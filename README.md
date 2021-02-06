# lb2120-telnet-reboot
Python script to remotely reboot Netgear LB2120 LTE modems via its integrated Telnet interface.

## Installation
1. Choose one of these methods:

    1. Script direct download (the simplest and shortest method):
        ```
        wget https://raw.githubusercontent.com/boonhui/lb2120-telnet-reboot/main/lb2120-telnet-reboot.py -O lb2120-telnet-reboot.py
        ```

    2. You can download the entire repository by using `git clone` or `git clone --depth 1 -b main` followed by the cloning URL above.

2. Enable diagnostics on the device to accept AT commands from the network:

    1. On the **LB2120 Manager** page, click **Settings > ADVANCED**.

	2. In the **LAN** pane, click **On** to **Enable Diagnostics**.

	3. Click **Submit**.

## Usage
```
lb2120-telnet-reboot.py <device ip or name>
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[GPLv3](https://choosealicense.com/licenses/gpl-3.0/)