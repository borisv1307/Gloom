## Quick Rulebook reference
- This is great for looking up how the random dungeon aspect of Gloomhaven works 
https://github.com/m-ender/gloomhaven-rules

## References
- The project we initially took inspiration from was: https://github.com/AluminumAngel/gloom 

- We used this https://www.redblobgames.com/grids/hexagons/ to handle the geometry on the backend
(Co-incidentally so do a lot of hexagrid based games on Github)


## Generating hexes
Library used: 
https://github.com/Hellenic/react-hexgrid

The [drag and drop example](https://github.com/Hellenic/react-hexgrid/tree/master/examples/drag-and-drop) is what Gloom started off using but we've changed the way how the hexes are generated. 
- Instead of statically generating the hexes and mapping the contents of each tile manually, we make a call to the Flask API server (http://localhost:5000/start) to get the JSON for constructed rooms

JSON structure:
Top level: Room ID
Nested within a room is the room name (Crossroads) and the list of tiles it holds.
Each tile has a sequential ID (0, 1, 2, ...), x,y,z co-ordinates for the tile along with the value it holds.
```
{
  "0": {
    "name": "Crossroads",
    "tiles": {
      "0": {
        "x": -2,
        "y": -3,
        "z": 5,
        "value": "entrance b"
      },
      "1": {
        "x": -1,
        "y": -3,
        "z": 4,
        "value": "empty"
      },
      "2": {
        "x": 0,
        "y": -3,
        "z": 3,
        "value": "empty"
      },
      "3": {
        "x": 1,
        "y": -3,
        "z": 2,
        "value": "empty"
      },
      "4": {
        "x": 2,
        "y": -3,
        "z": 1,
        "value": "hazardous terrain"
      },
      "5": {
        "x": 3,
        "y": -3,
        "z": 0,
        "value": "empty"
      },
      "6": {
        "x": 4,
        "y": -3,
        "z": -1,
        "value": "hazardous terrain"
    .
    .
    . (Truncated but this is the general layout)
  }
}
```

## Known issues with drag and drop
- Drag and drop works fine within the legend hexagons (on the right) since it's statically generated following the example in the react-hexgrid library
- However, the dynamically generated game hexagons (on the left) doesn't recognize drag and drop functions because of a mismatch in the way they are mapped vs the legend hexagons. 
- The library itself might not support the way we are generating the game hexagons because of the way it handles drag and drop using shallow copies instead of deep copies of the object. 

## Possible solutions
- Use Redux to handle state. The way React handles state gets very messy if we have a lot of components that make references to `this.state` or `this.props` 

    An example of how this potentially refactored to use Redux:
    - https://github.com/Codility/swarm


- Use a different library to handle generating and manipulating hexagons:
    - https://github.com/flauwekeul/honeycomb#api
    - https://github.com/mikegreer/hex-synth

- Use a different library to handle drag and drop (decouple from changing the way the hexagons are generated)
https://react-dnd.github.io/react-dnd/