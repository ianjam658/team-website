# Team Website Assignment — Work Log

## Repository

- **GitHub repository:** [ianjam658/team-website](https://github.com/ianjam658/team-website)
- **Default branch:** `main`
- **Website source folder:** `team-website/`
- **Development environment:** Kali Linux

## What the repository contains

The website is organized into HTML pages, CSS styling, and JavaScript behavior:

```text
team-website/
├── index.html
├── projects.html
├── contact.html
├── css/
│   └── styles.css
└── js/
    └── script.js
```

The repository also includes `create_zip.py`, a helper script for packaging the project, and this work-log document.

## What we did

1. Created the `team-website` GitHub repository.
2. Added the website files: home, projects, and contact pages, stylesheet, and JavaScript file.
3. Updated the names displayed on the site to our names. The team section on the home page shows **Ian Wafula** and **Evance Ochieng**; the site branding is **Team Byte**.
4. Added a Python helper to create a ZIP archive and this document describing the work and terminal workflow.

## Working from a Kali Linux terminal

The commands below show how to download the project, create its ZIP archive, and upload later edits. They assume Git and Python 3 are installed.

### Clone the repository

```bash
git clone https://github.com/ianjam658/team-website.git
cd team-website
```

### Create the ZIP archive

Run this from the repository's top-level folder:

```bash
python3 create_zip.py
```

This creates `team-website.zip` in the top-level folder. It includes the project and documentation, but excludes Git's internal `.git` directory and the generated archive itself. Run the command again whenever you want a fresh ZIP after making changes.

### Save and upload edits

After editing or adding files, use these commands from the repository folder:

```bash
git status
git add .
git commit -m "Update team website"
git push origin main
```

`git status` lets you review changes before staging them. The commit records changes locally, and `git push` uploads them to GitHub. GitHub may ask you to authenticate.

## Downloading a ZIP from GitHub

GitHub also provides a ZIP of the committed source: open the repository page, choose **Code**, then **Download ZIP**. The terminal script is useful for creating a fresh archive from your local working copy.
