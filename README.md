# Edoardo Fratus - Personal Portfolio

A personal portfolio website built with [Hugo](https://gohugo.io/) and the [Typo theme](https://github.com/tomfran/typo).

## About

This is the personal portfolio and tech blog of Edoardo Fratus, a software engineer passionate about distributed systems and cloud architecture. The site features blog posts, project showcases, and professional information.

## Tech Stack

- **Static Site Generator**: Hugo
- **Theme**: Typo by tomfran
- **Hosting**: GitHub Pages
- **Deployment**: GitHub Actions

## Prerequisites

- [Hugo](https://gohugo.io/installation/) (extended version)
- [Go](https://golang.org/doc/install) (for theme modules)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/edoofra/edoofra_personal_portfolio.git
cd edoofra_personal_portfolio
```

2. Install theme dependencies:
```bash
hugo mod get
```

## Development

Start the development server:
```bash
hugo server -D
```

The site will be available at `http://localhost:1313`

## Building

Generate the static site:
```bash
hugo
```

The generated site will be in the `public/` directory.

## Configuration

Main configuration is in `hugo.toml`. Key settings include:

- **Site info**: Title, description, base URL
- **Theme settings**: Color palette, appearance options
- **Social links**: LinkedIn, GitHub
- **Navigation menu**: Home, posts, about pages
- **Analytics**: Google Analytics integration

## Content Management

### Adding Posts

Create new posts in the `content/posts/` directory:
```bash
hugo new posts/my-new-post.md
```

### Content Structure

- `content/posts/` - Blog posts
- `static/` - Static assets (images, files)
- `layouts/` - Custom layout overrides
- `assets/` - Theme assets and customizations

## Deployment

The site is automatically deployed to GitHub Pages using GitHub Actions when changes are pushed to the master branch.

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

- **LinkedIn**: [Edoardo Fratus](https://www.linkedin.com/in/edoardofratus/)
- **GitHub**: [edoofra](https://github.com/edoofra)
- **Website**: [edoofra.github.io](https://edoofra.github.io)