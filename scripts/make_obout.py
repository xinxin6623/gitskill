#!/usr/bin/env python3
import os
import re
import shutil
import sys

def main():
    workspace_dir = "/Users/macmini/Documents/gitskill"
    src_dir = os.path.join(workspace_dir, "gitout")
    dst_dir = os.path.join(workspace_dir, "obout")

    print("=== Obsidian Vault Generator (gitout -> obout) ===")
    
    # Validate source dir
    if not os.path.exists(src_dir):
        print(f"Error: Source directory {src_dir} does not exist.")
        sys.exit(1)

    # 1. Clean and recreate destination directory
    if os.path.exists(dst_dir):
        print(f"Cleaning existing destination vault: {dst_dir}")
        shutil.rmtree(dst_dir)
    os.makedirs(dst_dir, exist_ok=True)

    # 2. Copy .obsidian configuration
    src_obsidian = os.path.join(src_dir, ".obsidian")
    dst_obsidian = os.path.join(dst_dir, ".obsidian")
    if os.path.exists(src_obsidian):
        print("Copying .obsidian configurations and plugins...")
        shutil.copytree(src_obsidian, dst_obsidian)
    else:
        print("Warning: .obsidian configuration folder not found in source.")

    # 3. Scan and map all files to build destination structure
    file_map = {}      # src_rel_path -> dst_rel_path
    all_md_files = []  # List of relative md paths
    other_files = []   # List of other files to copy

    for root, dirs, files in os.walk(src_dir):
        # Exclude 'raw' directory (contains raw HTML/markdown readmes)
        if 'raw' in root.split(os.sep):
            continue
        # Exclude internal folders manual copy
        if any(p in root.split(os.sep) for p in ['.obsidian', '.neural_db', '.neural_memory']):
            continue

        for f in files:
            if f.startswith('.'): # skip OS files like .DS_Store
                continue

            src_path = os.path.join(root, f)
            rel_path = os.path.relpath(src_path, src_dir)

            # Determine destination filename
            if f == "README.md" and rel_path != "README.md":
                # Rename domain README.md to <domain_name>.md to prevent name collision in Obsidian
                parent_dir = os.path.basename(os.path.dirname(src_path))
                dst_filename = f"{parent_dir}.md"
                dst_rel_path = os.path.join(os.path.dirname(rel_path), dst_filename)
            else:
                dst_rel_path = rel_path

            # Normalize paths to use forward slashes (standard for cross-platform)
            norm_rel_path = rel_path.replace(os.sep, '/')
            norm_dst_rel_path = dst_rel_path.replace(os.sep, '/')

            file_map[norm_rel_path] = norm_dst_rel_path
            
            if f.endswith(".md"):
                all_md_files.append(norm_rel_path)
            else:
                other_files.append(norm_rel_path)

    print(f"Found {len(all_md_files)} markdown files and {len(other_files)} other files to process.")

    # Link conversion statistics
    converted_links_count = 0
    external_links_count = 0
    local_anchors_count = 0
    missing_targets_count = 0

    # 4. Define conversion function
    def convert_links(src_rel_path, content):
        nonlocal converted_links_count, external_links_count, local_anchors_count, missing_targets_count
        
        def replace_link(match):
            nonlocal converted_links_count, external_links_count, local_anchors_count, missing_targets_count
            label = match.group(1)
            target = match.group(2).strip()

            # A. External links
            if target.startswith(("http://", "https://", "mailto:", "ftp:")):
                external_links_count += 1
                return match.group(0)

            # B. Local header anchor within the same file
            if target.startswith("#"):
                local_anchors_count += 1
                anchor_name = target[1:]
                return f"[[#{anchor_name}|{label}]]"

            # C. Relative file links
            current_src_dir = os.path.dirname(src_rel_path)

            # Extract anchor if present
            if '#' in target:
                target_path_part, anchor_part = target.split('#', 1)
                anchor = '#' + anchor_part
            else:
                target_path_part = target
                anchor = ''

            # Normalize relative target path relative to source file directory
            # os.path.normpath handles '../' and './' cleanly
            resolved_target = os.path.normpath(os.path.join(current_src_dir, target_path_part))
            resolved_target = resolved_target.replace(os.sep, '/')

            if resolved_target in file_map:
                dst_rel_target = file_map[resolved_target]
                # Path of the destination target relative to vault root, without extension
                target_vault_path = os.path.splitext(dst_rel_target)[0]
                converted_links_count += 1
                return f"[[{target_vault_path}{anchor}|{label}]]"
            else:
                # If target is raw/ or external to copied files, warn and keep as-is
                missing_targets_count += 1
                print(f"  [Warning] Link target '{target}' in '{src_rel_path}' could not be resolved.")
                return match.group(0)

        # Regex matches standard Markdown links: [Label](Target)
        pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
        return pattern.sub(replace_link, content)

    # 5. Process and copy markdown files
    print("Processing and converting markdown files...")
    for rel_path in all_md_files:
        src_path = os.path.join(src_dir, rel_path.replace('/', os.sep))
        dst_rel_path = file_map[rel_path]
        dst_path = os.path.join(dst_dir, dst_rel_path.replace('/', os.sep))

        os.makedirs(os.path.dirname(dst_path), exist_ok=True)

        with open(src_path, "r", encoding="utf-8") as f:
            content = f.read()

        new_content = convert_links(rel_path, content)

        with open(dst_path, "w", encoding="utf-8") as f:
            f.write(new_content)

    # 6. Copy other files (yaml, config, etc.)
    print("Copying remaining files...")
    for rel_path in other_files:
        src_path = os.path.join(src_dir, rel_path.replace('/', os.sep))
        dst_rel_path = file_map[rel_path]
        dst_path = os.path.join(dst_dir, dst_rel_path.replace('/', os.sep))

        os.makedirs(os.path.dirname(dst_path), exist_ok=True)
        shutil.copy2(src_path, dst_path)

    print("\n=== Conversion Completed Successfully! ===")
    print(f"Total Markdown Files: {len(all_md_files)}")
    print(f"Total Other Files:    {len(other_files)}")
    print(f"Converted Wiki-links: {converted_links_count}")
    print(f"External Links Kept:  {external_links_count}")
    print(f"Local Anchors Linked: {local_anchors_count}")
    print(f"Unresolved Links:     {missing_targets_count}")
    print(f"New Obsidian Vault is ready at: {dst_dir}\n")

if __name__ == "__main__":
    main()
