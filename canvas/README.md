## Prerequisites

### Install Homebrew

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Paste that in a Terminal prompt. Goto [Official Website](https://brew.sh/) to get more information.

### Install Node.js and npm

```
brew install node
```

Alternatively, goto [Official Website](https://nodejs.org/en/download/) to download the installer.

### Setup Local Server

```
npm install -g browser-sync
```

There are differnt ways to run a local server mentioned in [p5.js tutorial](https://github.com/processing/p5.js/wiki/Local-server), and `browser-sync` server which has the benefit of automatically reloading the webpage when any changes were saved in the source code.

## Launch the Canvas

The canvas has to been launched while the server is runing, or your drawing would not be able to received and saved.

```
browser-sync start --server -f -w
```

Press `[S]` to save your drawing or `[C]` to clear the canvas.
