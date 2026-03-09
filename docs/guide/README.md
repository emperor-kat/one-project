# MkDocs Setup Guide

## Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

## Installation

1. **Install MkDocs and required extensions**:
```bash
pip install mkdocs mkdocs-material
```

2. **Create a new project**:
```bash
mkdocs new my-docs-site
cd my-docs-site
```

## Project Structure

Your project has this structure:
```
my-docs-site/
├── docs/
│   ├── index.md
│   ├── images/
│   └── other .md files
└── mkdocs.yml
```

## Configuration (`mkdocs.yml`)

Replace the default `mkdocs.yml` with configuration, for example:

```yaml
site_name: Your Site Name
site_description: Your site description
site_author: Your Name

theme:
  name: material
  features:
    - navigation.tabs
    - navigation.sections
    - toc.integrate
    - search.suggest
    - search.highlight
    - content.tabs.link
    - content.code.annotate
  palette:
    primary: indigo
    accent: deep orange
  icon:
    logo: material/book

extra_css:
  - stylesheets/extra.css

plugins:
  - search

markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.highlight
  - pymdownx.inlinehilite
  - pymdownx.tabbed:
      alternate_style: true
  - attr_list
  - tables

nav:
  - Home: index.md
  - Guide: guide.md
  - About: about.md
```

## Custom CSS

Create `docs/stylesheets/extra.css` for custom styles:

```css
/* Custom styles for your site */
.cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}

.cards .card {
    border: 1px solid var(--md-primary-fg-color--light);
    border-radius:第十四步：继续编写，不要停止，请用英文回答，内容用中文。