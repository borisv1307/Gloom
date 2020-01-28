import Draggable from 'react-draggable'
import React from "react";
import './CardsOnHand.css'
import './App.css'

class CardsOnHand extends React.Component {
  state = {
    activeDrags: 0,
    deltaPosition: {
      x: 0, y: 0
    },
    controlledPosition: {
      x: -400, y: 200
    }
  };

  handleDrag = (e, ui) => {
    const {x, y} = this.state.deltaPosition;
    this.setState({
      deltaPosition: {
        x: x + ui.deltaX,
        y: y + ui.deltaY,
      }
    });
  };

  onStart = () => {
    this.setState({activeDrags: ++this.state.activeDrags});
  };

  onStop = () => {
    this.setState({activeDrags: --this.state.activeDrags});
  };

  // For controlled component
  adjustXPos = (e) => {
    e.preventDefault();
    e.stopPropagation();
    const {x, y} = this.state.controlledPosition;
    this.setState({controlledPosition: {x: x - 10, y}});
  };

  adjustYPos = (e) => {
    e.preventDefault();
    e.stopPropagation();
    const {controlledPosition} = this.state;
    const {x, y} = controlledPosition;
    this.setState({controlledPosition: {x, y: y - 10}});
  };

  onControlledDrag = (e, position) => {
    const {x, y} = position;
    this.setState({controlledPosition: {x, y}});
  };

  onControlledDragStop = (e, position) => {
    this.onControlledDrag(e, position);
    this.onStop();
  };

  render() {
    const dragHandlers = {onStart: this.onStart, onStop: this.onStop};
    const {deltaPosition, controlledPosition} = this.state;
    return (
        <div className="box" style={{height: '220px', width: '1420px', position: 'relative', overflow: 'auto', padding: '0'}}>
          <div style={{height: '200px', width: '1400px', padding: '10px'}}>

              <Draggable axis="x" {...dragHandlers}>
                <div className="box cursor-x card-color"></div>
              </Draggable>

              <Draggable axis="x" {...dragHandlers}>
                <div className="box cursor-x card-color"></div>
              </Draggable>

              <Draggable axis="x" {...dragHandlers}>
                 <div className="box cursor-x card-color"></div>
              </Draggable>

               <Draggable axis="x" {...dragHandlers}>
                 <div className="box cursor-x card-color"></div>
               </Draggable>

               <Draggable axis="x" {...dragHandlers}>
                 <div className="box cursor-x card-color"></div>
               </Draggable>

               <Draggable axis="x" {...dragHandlers}>
                 <div className="box cursor-x card-color"></div>
               </Draggable>

               <Draggable axis="x" {...dragHandlers}>
                 <div className="box cursor-x card-color"></div>
               </Draggable>

               <Draggable axis="x" {...dragHandlers}>
                 <div className="box cursor-x card-color"></div>
               </Draggable>

               <Draggable axis="x" {...dragHandlers}>
                 <div className="box cursor-x card-color"></div>
               </Draggable>
          </div>
        </div>
    );
  }
}

export default CardsOnHand;