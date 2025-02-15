FILE_TYPES = {
    "css": ["style", "main", "theme", "layout", "responsive", "dark-mode", "animation", "grid", "typography", "custom", "reset", "buttons", "forms", "header", "footer"],
    "html": ["index", "about", "contact", "services", "portfolio", "blog", "team", "faq", "testimonials", "pricing", "privacy-policy", "terms-of-service", "careers", "support", "newsletter"],
    "docx": ["resume", "report", "proposal", "contract", "meeting-notes", "whitepaper", "business-plan", "case-study", "press-release", "research-paper", "invoice", "manual", "presentation", "brochure", "letter"],
    "php":["config","index","main","registration","submit","authorization","db","connection"],
    "pdf": ["manual", "ebook", "invoice", "guide", "whitepaper", "presentation", "catalog", "brochure", "flyer", "report", "portfolio", "resume", "proposal", "datasheet", "specifications"],
    "txt": ["readme", "notes", "log", "changelog", "todo", "draft", "summary", "memo", "outline", "backup", "transcript", "diary", "journal", "instructions", "manifesto"],
    "jpg": ["photo", "background", "logo", "banner", "portrait", "wallpaper", "illustration", "snapshot", "thumbnail", "cover", "profile", "advertisement", "screenshot", "flyer", "poster"],
    "png": ["icon", "banner", "screenshot", "avatar", "button", "logo", "illustration", "sticker", "badge", "watermark", "overlay", "diagram", "infographic", "thumbnail", "chart"],
    "js": ["script", "app", "functions", "utilities", "events", "dom-manipulation", "ajax", "api-calls", "validation", "form-handler", "animations", "effects", "game", "config", "router"],
    "py": ["script", "main", "config", "utils", "data-processing", "web-scraper", "machine-learning", "automation", "crawler", "server", "flask-app", "django-project", "cli-tool", "bot", "notebook"],
    "json": ["data", "config", "settings", "localization", "translations", "schema", "manifest", "metadata", "user-preferences", "cache", "api-response", "mock-data", "database", "permissions", "logs"],
    "xml": ["feed", "sitemap", "data", "schema", "rss", "config", "settings", "manifest", "response", "export", "import", "theme", "translations", "ui-elements", "metadata"],
    "zip": ["backup", "archive", "project", "source-code", "compressed", "dataset", "export", "import", "resources", "templates", "installation", "bundle", "package", "release", "repository"],
    "mp3": ["song", "podcast", "audio", "recording", "voiceover", "interview", "audiobook", "lecture", "meditation", "music", "soundtrack", "background-music", "sample", "jingle", "alarm"],
    "mp4": ["video", "movie", "clip", "tutorial", "presentation", "animation", "documentary", "gameplay", "review", "promo", "advertisement", "music-video", "stream", "recording", "vlog"],
    "csv": ["data", "records", "export", "transactions", "inventory", "sales", "report", "database", "log", "user-list", "products", "tracking", "attendance", "metrics", "analytics"]
}

DIRECTORIES = {
    "web": {"files": ["html", "css", "php"], "directories": ["css", "data", "templates", "js", "assets"]},
    "documents": {"files": ["docx", "pdf", "txt"], "directories": ["reports", "invoices", "manuals", "letters", "drafts"]},
    "media": {"files": ["jpg", "png", "mp4", "mp3"], "directories": ["images", "videos", "audio", "thumbnails", "backgrounds"]},
    "scripts": {"files": ["js", "py", "sh"], "directories": ["python", "javascript", "shell", "batch", "automation"]},
    "data": {"files": ["csv", "json", "xml"], "directories": ["exports", "imports", "logs", "backups", "raw"]},
    "projects": {"files": ["zip", "txt", "json"], "directories": ["archives", "source", "compiled", "modules", "docs"]},
    "server": {"files": ["config", "log", "json"], "directories": ["nginx", "apache", "database", "cache", "backups"]},
    "videos": {"files": ["mp4","avi","mkv"], "directories": []},
    "audio": {"files": ["mp3","ogg","way","flac"], "directories": []},
    "backgrounds": {"files": ["jpg","png","webp"], "directories": []},
    "python": {"files": ["py","json","md"], "directories": []},
    "javascript": {"files": ["js","map","json"], "directories": []},
    "exports": {"files": ["csv","xlsx","txt","log","json"], "directories": []},
    "logs": {"files": ["json","txt","log"], "directories": []},
    "database": {"files": ["sql","sqlite","db"], "directories": []}
}

CURSES_OPTIONS = [
    {
        "title":"Welcome to HoneypotFTP!",
        "key":"c",
        "text":"Show current connections"
    },
    {
        "title":"Server configuration",
        "key":"s",
        "text":"Show server configuration"
    },
    {
        "title":"Log file explorer",
        "key":"l",
        "text":"Show created log files"
    },
    {
        "title":"Quit HoneypotFTP",
        "key":"q",
        "text":"Quit HoneypotFTP"
    }
]