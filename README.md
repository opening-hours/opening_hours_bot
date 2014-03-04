# opening_hours bot

This repository keeps track of scripts I use to speed up the Quality Assurance process of [opening\_hours][key:opening\_hours] values. Although the repository has the word 'bot' in it, the scripts do not yet (if ever) run as bot. I do review every change which are made by these scripts. Additionally all changes are automatically checked using the [opening_hours.js][oh-lib] library (old value must be an error and the new one must be ok without any warnings).

[key:opening\_hours]: http://wiki.openstreetmap.org/wiki/Key:opening_hours
[oh-lib]: https://github.com/ypid/opening_hours.js

## Install

Just clone the repository with

```
git clone --recursive https://github.com/ypid/opening_hours_bot.git
```

and install it’s dependencies (execute inside the repository):
```
cd pyopening_hours/ && npm install
```

## Usage
The script OpeningHoursBot.py can be called with an [OSM XML](http://wiki.openstreetmap.org/wiki/OSM_XML) file as parameter and will write a corrected "$basename-fixed.osm" file.
