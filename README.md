# Admin How-To Guides

Client-facing how-to guides (static HTML/CSS) published with GitHub Pages.

- Edit the page content in `content/*.html`, then run `python3 build.py` to regenerate the top-level pages.
- Screenshots are in `assets/img/`.
- Deployment: `.github/workflows/pages.yml` publishes the repo root to GitHub Pages on every push to `main`. One-time setup: in the repo, go to Settings › Pages › Source and choose **GitHub Actions**.
