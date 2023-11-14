# oneshot-web

## Deployment of oneshot-web

Please check out the [deployment instructions](DEPLOY.md) if you want to self-host oneshot-web.

## Development Setup

1. clone the repository
2. open folder in vscode
3. install recommended extensions
4. reopen in container
5. type `make` to see what you can do (e. g. how to build the docker image from source)

### Start the backend

1. `make start-api`

### Start the frontend

1. `make start-frontend`

### PWA Dev Setup

1. `cd frontend`
2. Make sure `devOptions { enabled: true }` is set in `vite.config.js`
3. Run 'npm run build' to generate the service worker and manifest in the `dist` folder (production build) and `dist-dev` (dev build)
4. Run `npm run dev`\ `npm run preview`, the pwa should now appear as installable in the browser

#### Checking PWA requirements, usability and performance

1. Install Chrome
2. Install Google Lighthouse extension
3. Open dev tools (F12) and go to the Lighthouse tab
4. Run the audit
