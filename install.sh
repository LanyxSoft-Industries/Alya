is_user_root() { [ "$(id -u)" -eq 0 ]; }
if is_user_root; then
    echo "Starting install script."
else
    echo "Please run with root."
    exit;
fi

LANYXSOFT_DIVISION="Alya"
PROGRAM="meets"

MACHINE_TYPE="`uname -m`"
case $MACHINE_TYPE in
    'x86_64')
        MACHINE_TYPE='x86_64'
        ;;
    *)
        MACHINE_TYPE='unknown'
        ;;
esac

# Linux Core Functions
lm_core_d() {
    if [ ! -d "/usr/share/lanyxsoft" ]
    then
        echo "Creating driectory 'lanyxsoft' in '/usr/share'"
        mkdir "/usr/share/lanyxsoft"
    fi
    if [ -d "/usr/share/lanyxsoft" ]
    then
        if [ ! -d "/usr/share/lanyxsoft/$LANYXSOFT_DIVISION" ]
        then
            echo "Creating driectory '$LANYXSOFT_DIVISION' in '/usr/share/lanyxsoft'"
            mkdir "/usr/share/lanyxsoft/$LANYXSOFT_DIVISION"
        fi
    fi
    if [ -d "/usr/share/lanyxsoft" ]
    then
        if [ ! -d "/usr/share/lanyxsoft/$LANYXSOFT_DIVISION/$PROGRAM" ]
        then
            echo "Creating driectory '$PROGRAM' in '/usr/share/lanyxsoft/$LANYXSOFT_DIVISION'"
            mkdir "/usr/share/lanyxsoft/$LANYXSOFT_DIVISION/$PROGRAM"
        fi
    fi
}

ld_core_f() {
    if ! ls "/usr/share/lanyxsoft/$LANYXSOFT_DIVISION/$PROGRAM/crontab_template.txt" > /dev/null
    then
        wget -q "https://raw.githubusercontent.com/LanyxSoft-Industries/Alya_Google-Meets-Automation/main/crontab_template.txt"
    else
        echo "File already exists, not updating"
    fi
    if ! ls "/usr/share/lanyxsoft/$LANYXSOFT_DIVISION/$PROGRAM/meet.py" > /dev/null
    then
        wget -q "https://raw.githubusercontent.com/LanyxSoft-Industries/Alya_Google-Meets-Automation/main/meet.py"
    else
        echo "File already exists, not updating"
    fi
    if ! ls "/usr/share/lanyxsoft/$LANYXSOFT_DIVISION/$PROGRAM/schedule.json" > /dev/null
    then
        wget -q "https://raw.githubusercontent.com/LanyxSoft-Industries/Alya_Google-Meets-Automation/main/schedule.json"
    else
        echo "File already exists, not updating"
    fi
    if ! ls "/usr/share/lanyxsoft/$LANYXSOFT_DIVISION/$PROGRAM/schedule_reset.py" > /dev/null
    then
        wget -q "https://raw.githubusercontent.com/LanyxSoft-Industries/Alya_Google-Meets-Automation/main/schedule_reset.py"
    else
        echo "File already exists, not updating"
    fi
    if ! ls "/usr/share/lanyxsoft/$LANYXSOFT_DIVISION/$PROGRAM/scheduler.py" > /dev/null
    then
        wget -q "https://raw.githubusercontent.com/LanyxSoft-Industries/Alya_Google-Meets-Automation/main/scheduler.py"
    else
        echo "File already exists, not updating"
    fi
    echo "File download complete!"
}

case "`uname`" in
    'Linux')
        OS='Linux'
        
        cd "/usr/share"
        lm_core_d
        cd "lanyxsoft/$LANYXSOFT_DIVISION/$PROGRAM"
        echo "Creating initialization log file."
        echo "Timestamp: `date`\n------> User: $USER\n------> `sudo dmidecode | grep -A3 '^System Information'`\n`uname -r` | `uname -v` on `uname -o`\n------> Node Name: `uname -n`\n" >> "LanyxSoft Alya Initialization.log"
        echo "Downloading files from Github [https://github.com/LanyxSoft-Industries/Alya_Google-Meets-Automation]..."
        ld_core_f
        if [ ! -e "/etc/cron.d/lanyxsoft_${LANYXSOFT_DIVISION}_google-meets-automation" ]
        then
            echo "Creating cron task [/etc/cron.d/lanyxsoft_${LANYXSOFT_DIVISION}_google-meets-automation]"
            echo "*/5 * * * 1-5 root export DISPLAY=:0 && export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/bin && /usr/bin/python3 /usr/share/lanyxsoft/Alya/meets/scheduler.py >> /usr/share/lanyxsoft/Alya/meets/scheduler.log" >> "/etc/cron.d/lanyxsoft_${LANYXSOFT_DIVISION}_google-meets-automation"
        fi
        ;;
    'FreeBSD')
        OS='FreeBSD'

        echo "Not implimented yet. :\"
        exit;
        ;;
    'WindowsNT')
        OS='Windows'

        echo "Not implimented yet. :\"
        exit;
        ;;
    'Darwin') 
        OS='Mac'

        echo "Not implimented yet. :\"
        exit;
        ;;
    'SunOS')
        OS='Solaris'

        echo "Not implimented yet. :\"
        exit;
        ;;
    'AIX')
        OS='AIX'

        echo "Not implimented yet. :\"
        exit;
        ;;
    *)
        OS='unknown'

        echo "Not implimented yet. :\"
        exit;
        ;;
esac

# cd /usr/share
# echo "`ls`"