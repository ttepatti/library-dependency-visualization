# library-dependency-visualization

These are scripts and chunks of data for testing out black-box library dependency visualization/graphing.

The goal of these tools is to allow for identification of potentially interesting or even vulnerable functionality within black box firmware binaries. If you see a number of binaries or libraries that don't seem to be referenced by the wider system, it could point to areas of 3rd party code that may be interesting to hunt for vulnerabilities in.

The scripts and data here are in development/WIPs, I do not recommend using any of them for serious purposes. These are simply fun tech demos!

Long term goal: I'd like to incorporate this functionality into the [elf-analyzer](https://github.com/ttepatti/elf-analyzer) tool.
