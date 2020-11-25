LANYXSOFT_DIVISION="Alya"
PROGRAM="meets"
MACHINE_TYPE="`uname -m`"

is_user_root() { [ "$(id -u)" -eq 0 ]; }
if is_user_root; then
    echo "Starting uninstall script."
else
    echo "Please run with root."
    exit;
fi

case $MACHINE_TYPE in
    'x86_64')
        MACHINE_TYPE='x86_64'
        ;;
    *)
        MACHINE_TYPE='unknown'
        ;;
esac

# Linux Core Functions
ld_core_d() {
    if [ ! -d "/usr/share/lanyxsoft" ]
    then
        echo "[ERROR]: Base directory 'lanyxsoft' was not found. Creating it now in '/usr/share'..."
        mkdir "/usr/share/lanyxsoft"
    fi
    if [ -d "/usr/share/lanyxsoft" ]
    then
        if [ -d "/usr/share/lanyxsoft/$LANYXSOFT_DIVISION" ]
        then
            echo "Removing '${LANYXSOFT_DIVISION}' core directory..."
            rm -r "/usr/share/lanyxsoft/${LANYXSOFT_DIVISION}"
        else
            echo "[ERROR]: Core directory '${LANYXSOFT_DIVISION}' was not found. Assuming uninstallation completion status: TRUE"
            exit;
        fi
    fi
}

case "`uname`" in
    'Linux')
        OS='Linux'

        if [ -e "/etc/cron.d/lanyxsoft_${LANYXSOFT_DIVISION}_google-meets-automation" ]
        then
            echo "Removing cron task [/etc/cron.d/lanyxsoft_${LANYXSOFT_DIVISION}_google-meets-automation]"
            rm "/etc/cron.d/lanyxsoft_${LANYXSOFT_DIVISION}_google-meets-automation"
        fi
        echo "Deleting ${LANYXSOFT_DIVISION} core directories and installed files."
        ld_core_d
        ;;
    'FreeBSD')
        OS='FreeBSD'

        echo "Not implimented yet. :\\"
        exit;
        ;;
    'WindowsNT')
        OS='Windows'

        echo "Not implimented yet. :\\"
        exit;
        ;;
    'Darwin') 
        OS='Mac'

        echo "Not implimented yet. :\\"
        exit;
        ;;
    'SunOS')
        OS='Solaris'

        echo "Not implimented yet. :\\"
        exit;
        ;;
    'AIX')
        OS='AIX'

        echo "Not implimented yet. :\\"
        exit;
        ;;
    *)
        OS='unknown'

        echo "Not implimented yet. :\\"
        exit;
        ;;
esac