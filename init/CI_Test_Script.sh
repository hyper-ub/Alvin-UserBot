export SEMAPHORE_PROJECT_DIR=`pwd`
. "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")"/telegram
TELEGRAM_TOKEN=${BOT_API_KEY}
export BOT_API_KEY TELEGRAM_TOKEN
tg_sendinfo "<code>I am gonna merge staging into Lord-Userbot</code>"
cd
git clone https://github.com/mkaraniya/OpenUserBot.git
cd OpenUserBot
git remote set-url origin https://${GH_USERNAME}:${GH_PERSONAL_TOKEN}@github.com/mkaraniya/OpenUserBot.git
git fetch
git checkout staging
git pull origin staging
git push --force origin staging:Alvin-Userbot
tg_sendinfo "<code>I have merged all commits from staging into Lord-Userbot</code>"
