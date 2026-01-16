---
name: rclone
description: Upload files to cloud storage (S3, R2, B2, etc.)
argument-hint: "[file(s)] [remote:path]"
---

# Rclone

Upload, sync, and manage files across cloud storage providers.

## Input

<args> #$ARGUMENTS </args>

## Common Operations

### Upload file
```bash
rclone copy /path/to/file remote:bucket/path/
```

### Upload directory
```bash
rclone copy /path/to/dir remote:bucket/path/ --progress
```

### Sync (mirror)
```bash
rclone sync /local/path remote:bucket/path/
```

### List remotes
```bash
rclone listremotes
```

### List files
```bash
rclone ls remote:bucket/path/
```

## Supported Providers

- Amazon S3
- Cloudflare R2
- Backblaze B2
- Google Drive
- Dropbox
- And 40+ more

## Setup

If rclone isn't configured, guide the user:
```bash
rclone config
```

## Examples

- `/rclone ./image.png r2:mybucket/images/`
- `/rclone ./dist/ s3:mybucket/releases/ --progress`
- `/rclone listremotes`
