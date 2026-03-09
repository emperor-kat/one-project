# MkDocs Project Setup Guide


## Prerequisites

Before you begin, ensure you have the following installed on your system:
- Python (version 3.6 or higher)
- pip (Python package manager, usually comes with Python)

## Step 1: installation

Install MkDocs and the Material for MkDocs theme using pip:

```bash
pip install mkdocs-material
```

## Step 2: create new project

Initialize a new MkDocs project in a folder of your choice.

```bash
mkdir my-mkdocs-site
cd my-mkdocs-site

mkdocs new .
```

## Step 3: project structure

Your project has this structure:
```
my-mkdocs-site/
    ├── docs/
    │    ├── index.md
    │    └── images/
    └── mkdocs.yml
```

## Step 4: configuration (`mkdocs.yml`)

Replace the contents of `mkdocs.yml` with this configuration:

```yaml
site_name: My MkDocs Site
site_description: A modern documentation website built with MkDocs
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

## Step 5: custom styling

Create custom CSS file:

```bash
mkdir docs/stylesheets
touch docs/stylesheets/extra.css
```

## Step 6: serve your site locally

Run from your project's root directory:

```bash
mkdocs serve
```

Your site will be available at `http://127.0.0.1:8000`.

## Step 7: content creation

### Images
```markdown
![Description of image](images/my-image.jpg)

<img src="images/my-image.jpg" alt="Description" width="300" align="right">
```

### Tabs
````markdown
=== "Tab 1"
    Content for the first tab.

=== "Tab 2"
    Content for the second tab.

    ```python
    print("Code in tabs!")
    ```
````

### Hints
```markdown
!!! note
    This is a neutral note.

!!! abstract "Custom Title"
    This is a summary with a custom title.

!!! success
    This indicates a successful action.

!!! warning
    This is a warning.

!!! danger
    This is a dangerous thing.
```

### Links
```markdown
[Link Text](guide.md)
[Link to header](guide.md#specific-header)

[OpenAI](https://www.openai.com)

<a href="https://www.openai.com" target="_blank">OpenAI (New Tab)</a>
```

### Code Blocks
````markdown
```python
def hello_world():
    print("Hello, World!")
```

```python title="hello.py"
def hello_world():
    print("Hello, World!")
```
````

## Step 8: build and deploy

```bash
mkdocs build

mkdocs gh-deploy
```