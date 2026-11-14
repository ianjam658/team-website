# Team Website Assignment — Work Log

## Repository

- GitHub repository: https://github.com/ianjam658/team-website
- Branch: `main`
- Operating system used: Kali Linux
- Project folder: `team-website/`

## Project summary

This assignment was to create a basic team website using HTML, CSS, and JavaScript, push it to GitHub, and document the work. We created the repository, added the website files, changed the sample text to reflect our own names and information, and created a ZIP archive of the finished project.

The website files contain the layout, styling, and script behavior for the pages:

```text
team-website/
├── index.html
├── projects.html
├── contact.html
├── css/
│   └── styles.css
├── js/
│   └── script.js
├── create_zip.py
├── ASSIGNMENT.md
└── team-website.zip
```

## What we changed on the site

We updated the placeholder names and content to match our own team information.

- Home page team section includes: **Ian Wafula** and **Evance Ochieng**
- The site uses the label **Team Byte** as the project brand
- The content was customized to describe our team and the assignment work

This was done directly in the HTML files so the website displayed our names instead of the original sample text.

## What we did from the terminal

The following commands show the workflow we used on Kali Linux to set up the project, add files, and upload them to GitHub.

### 1. Create the project folder

```bash
mkdir team-website
cd team-website
```

### 2. Initialize Git

```bash
git init
git branch -M main
```

### 3. Add the website files

After creating or editing the HTML, CSS, and JavaScript files, stage them:

```bash
git add .
```

### 4. Commit the project

```bash
git commit -m "Initial team website commit"
```

### 5. Connect to GitHub

```bash
git remote add origin https://github.com/ianjam658/team-website.git
```

### 6. Push to GitHub

```bash
git push -u origin main
```

### 7. Create a ZIP archive

From the project root, run:

```bash
python3 create_zip.py
```

This creates a ZIP file named `team-website.zip` in the project directory. The helper script excludes the `.git` folder and the ZIP itself so the archive contains only project files.

## ZIP generation script

The repository includes a Python script named `create_zip.py` that builds the archive. It scans the project folder, includes all files except `.git` and the archive being created, and writes them into a ZIP file.

Example:

```bash
python3 create_zip.py
ls -l
```

This verifies that the ZIP was created successfully.

## Final assignment notes

The completed work includes:

- GitHub repository created
- Team website files added
- Names changed to ours
- Project archived as a ZIP file
- Assignment documentation created

This assignment was completed in Kali Linux using the terminal for version control and archive creation, and the final project was uploaded to GitHub.
