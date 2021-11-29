### **Requirements:** 🔌
  - Docker
  - Docker-compose

### **Steps:**
  - Edit the `.env` file if necessary
  - Run the project installer: `make install`

### **Commands:** 📄
  - `make up` - Builds the containers
  - `make start`- Starts all on.ge containers
  - `make stop`- Stops all on.ge containers
  - `make shell <SERVICE NAME>`- Opens a shell console of a service (example: make shell on.website)
  - `make logs`- Open log for on.ge containers
  - `make kill`- Destroy on.ge containers
  - `make prune` - Stop and destroy all on.ge containers

### **URL:** 🗺️
  - `on.localhost` - Main site
  - `admin.on.localhost` - Admin panel
  - `pma.on.localhost` - PhpMyAdmin
  - `monitor.on.localhost` - Traefik web-UI
  - `docs.on.localhost` - Documentations

---
#### 🔔 More content is coming...
**Maintainer:** Temuri Takalandze <t.takalandze@omedia.dev>