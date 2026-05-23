# Modern Developer Blog Template (Digital Garden Starter)

![GardenPromo](/screenshots/garden-promo.jpg)
[More screenshots here](/screenshots/)

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fthedevdavid%2Fdigital-garden%2F)

An open source blogging (digital gardening) template for developers using [Next.js](https://nextjs.org/) app router, MDX, [Contentlayer](https://contentlayer.dev/), [Tailwind CSS](https://tailwindcss.com/), [@shadcn/ui](https://ui.shadcn.com/) , [Lucide Icons](https://lucide.dev/icons), and more.

If you love this template and/or use it, please give it a star on GitHub. This will help more people discover it, thus help improving the template.

![GitHub Repo stars](https://img.shields.io/github/stars/thedevdavid/digital-garden?style=social)

**Note: This project is always evolving and it's far from being perfect or even done.** I'm always open to suggestions and contributions. Feel free to open an issue or a PR if you have any ideas or suggestions. You can also see the [roadmap](#features--roadmap) for planned features if you want to contribute.

## Table of Contents

- [Motivation](#motivation)
- [Getting Started](#getting-started)
  - [Writing content](#writing-content)
    - [Frontmatter](#frontmatter)
  - [Deployment](#deployment)
- [Customization](#customization)
  - [Fonts](#fonts)
  - [Colors](#colors)
  - [Signature](#signature)
  - [Images](#images)
    - [Homepage Avatar](#homepage-avatar)
  - [Metadata](#metadata)
    - [Navigation](#navigation)
    - [Social links](#social-links)
  - [Analytics](#analytics)
    - [Vercel](#vercel)
    - [Umami](#umami)
    - [Plausible](#plausible)
    - [Google Analytics](#google-analytics)
    - [Other analytics providers](#other-analytics-providers)
  - [Newsletter subscription](#newsletter-subscription)
    - [MailerLite](#mailerlite)
    - [Other newsletter providers](#other-newsletter-providers)
  - [Hero section](#hero-section)
  - [Other tips & tricks](#other-tips--tricks)
    - [Image optimization](#image-optimization)
- [Examples](#examples)
- [Features & Roadmap](#features--roadmap)
- [Contributing](#contributing)
  - [Contributors](#contributors)
  - [How?](#how)
- [Inspiration & Mentions](#inspiration--mentions)
- [Support](#support)

## Motivation

As a developer who creates content, I want to have a blog & digital garden where I can share my thoughts and ideas with the world. Now, there's not really a "perfect solution" for this currently. With included analytics, SEO, email subscriptions, modern tooling, simple design, etc. We either have to build one from scratch, use a design template and code the features, or use a CMS/no-code tool.

So I decided to build a solution that I would use myself. This is the result.

## Getting Started

If you want to see how I set up this template for my own digital garden, you can check out [this commit](https://github.com/thedevdavid/website-2023/commit/fb10942d424a1389f9c4c1605849e45ff718656d) with all the changes.

1. Use the repo as a template
2. Install dependencies with `pnpm install`
3. Edit `utils/metadata.ts` with your information and general settings
4. Edit `utils/uses-data.ts` with software & hardware you use
5. Edit `utils/projects-data.ts` with your projects
6. Edit `utils/navigation-links.ts` with the links you want in the navigation
7. Edit `content/pages/now` with your availability
8. Edit `content/pages/about` with your bio
9. Run the development server with `pnpm dev`

Open [http://localhost:3000](http://localhost:3000) in your browser to see the result.

### Writing content

You can write content in Markdown or MDX. The content is located in `content/` and is organized in folders. The `pages` folder contains the pages. The `posts` folder contains the blogposts. The `projects` folder contains the projects.

Editing list pages is done in the `lib` folder.

- `/uses` - `lib/uses-data.ts`
- `/projects` - `lib/projects-data.ts`
- `/social` - `lib/social-data.ts`

#### Frontmatter

Frontmatter is used to define metadata for pages and posts. It's located at the top of the file and is written in YAML. You can define the following fields:

- `title` - The title of the page/post
- `description` - The description of the page/post
- `publishedDate` - The date of the post (not used on pages)
- `lastUpdatedDate` - The date of the page/post
- `tags` - List of tags for the post. You can add new tags by adding them to the `tagOptions` list. (not used on pages)
- `series` - The series of the post. A series has a title and an order number for a post. (not used on pages)
- `author` - The author of the post. An author has a name, and image. (not used on pages)
- `status` - Whether the page/post is published or draft

### Deployment

You can deploy the project with [Vercel](https://vercel.com/) or any other hosting provider. If you want to use Vercel, you can use the button at the top of this README.

1. Update `package.j