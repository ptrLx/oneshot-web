# oneshot-web

## Development Setup

1. clone the repository
2. open folder in vscode
3. install recommended extensions
4. reopen in container

### Start the backend

1. `make start-api`

### Start the frontend

1. `make start-frontend`


### PWA Dev Setup

1. `cd frontend`
2. Make sure `devOptions { enabled: true}` is set in `vite.config.js`
3. Run 'npm run build' to generate the service worker and manifest in the `dist` folder
4. Run `npm run dev`, the pwa should now appear as installable in the browser

#### Checking PWA requirements, usability and performance
1. Install Chrome
2. Install Google Lighthouse extension
3. Open dev tools (F12) and go to the Lighthouse tab
4. Run the audit

