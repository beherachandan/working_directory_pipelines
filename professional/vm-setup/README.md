# VM Setup: Claude Code + OpenClaw

## What is OpenClaw?
Open-source, self-hosted personal AI assistant. Runs on your VM, connects to
WhatsApp/Telegram/Discord/Slack/Signal, has persistent memory, can run shell
commands, browse the web, and write its own plugins. Supports Claude as the AI backend.

---

## Prerequisites (local machine)
- Instance ID (e.g., `i-0abc123` for AWS, or GCP instance name)
- SSH private key file (`.pem` or `.key`)
- Anthropic API key (`sk-ant-...`)

---

## Step 1: Set key permissions

```bash
chmod 400 /path/to/your-key.pem
```

---

## Step 2: Get your VM's public IP

**AWS:**
```bash
aws ec2 describe-instances --instance-ids <INSTANCE_ID> \
  --query 'Reservations[0].Instances[0].PublicIpAddress' --output text
```

**GCP:**
```bash
gcloud compute instances describe <INSTANCE_NAME> \
  --format='get(networkInterfaces[0].accessConfigs[0].natIP)'
```

---

## Step 3: SSH into the VM

```bash
ssh -i /path/to/your-key.pem ubuntu@<PUBLIC_IP>
# Amazon Linux → ec2-user | Debian → admin
```

---

## Step 4: System setup inside the VM

```bash
sudo apt update && sudo apt upgrade -y

# Install Node.js 20
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs

# Install tmux (keeps sessions alive after SSH disconnect)
sudo apt install -y tmux
```

Start a persistent session:
```bash
tmux new -s main
# To reconnect later: tmux attach -t main
```

---

## Step 5: Install Claude Code CLI

```bash
npm install -g @anthropic-ai/claude-code
claude --version
```

Set your API key:
```bash
export ANTHROPIC_API_KEY="sk-ant-..."
echo 'export ANTHROPIC_API_KEY="sk-ant-..."' >> ~/.bashrc
```

Test it:
```bash
claude
```

---

## Step 6: Install OpenClaw

```bash
# Option A — one-liner installer
curl -fsSL https://openclaw.ai/install.sh | bash

# Option B — npm
npm i -g openclaw
```

Run onboarding (connects your chat apps + sets Claude as backend):
```bash
openclaw onboard
```

During onboarding:
- Choose **Anthropic Claude** as your AI model
- Paste your `ANTHROPIC_API_KEY`
- Connect chat platforms (Telegram/WhatsApp/Slack etc.)

---

## Step 7: Run OpenClaw in the background

```bash
# Inside your tmux session
openclaw start

# Detach tmux (session keeps running after you close SSH)
# Ctrl+B, then D
```

---

## Useful commands

| Command | What it does |
|---|---|
| `openclaw start` | Start the assistant daemon |
| `openclaw stop` | Stop the daemon |
| `openclaw status` | Check if running |
| `openclaw logs` | View recent activity |
| `tmux attach -t main` | Re-enter your session |

---

## Notes
- OpenClaw stores memory locally on the VM — data never leaves your server
- To expose it to the internet securely, consider adding a reverse proxy (nginx + SSL)
- Heartbeats (cron jobs) let OpenClaw proactively message you on a schedule
