# gedcom-to-map

convert Gedcom to KML file
 _geographic coordinates must be provided in GEDCOM file_
 
 
 ### Usage
 
 ```
gedcom-to-map.py [-h] [--max_missing MAX_MISSING]
                        [--max_line_weight MAX_LINE_WEIGHT]
                        input_file output_file main_entity
```

### Exemple


* Input : [sample/intput.kml](https://github.com/lmallez/gedcom-to-map/blob/master/samples/input.ged)
![img](https://github.com/lmallez/gedcom-to-map/blob/master/samples/input.png)

`gedcom-to-map.py samples/input.ged samples/output.kml @I0000@`

* Output : [sample/output.kml](https://github.com/lmallez/gedcom-to-map/blob/master/samples/output.kml)
![img](https://github.com/lmallez/gedcom-to-map/blob/master/samples/output.png)
