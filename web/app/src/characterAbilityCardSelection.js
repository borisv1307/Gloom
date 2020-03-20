import React, {Component} from 'react'
import ReactDOM from "react-dom";
import './characterAbilityCardSelection.css'
import BRUTE from './bruteAbilityCardimages'
import App from "./App";
import backImg from "./back_red.png"
import ItemSelection from "./itemSelection";
import items from "./itemsList";


let selectedImages;
selectedImages = [];
let maxCardsInHand;
let items_selected;

const CharacterAbilityBox = (props) => {

    function displayCharacterSelected() {
      // ReactDOM.render(<CharacterAbilityCardSelection characterName={props.characterName} characterCardHand={props.characterCardHand}/>, document.getElementById('root'));
        //alert('Hey!');

        let isChecked = false;
        items_selected = document.getElementById("items_hidden").value;
        for(let i =0;i<selectedImages.length;i++)
        {
            if(props.characterCardId == selectedImages[i])
            {
                isChecked=true;
                selectedImages.splice(i,1);
                document.getElementById(props.characterCardId).className = 'characterAbilityBox'
            }
        }

        if (selectedImages.length<maxCardsInHand)
        {
            if(!isChecked)
            {
                selectedImages.push(props.characterCardId);
                document.getElementById(props.characterCardId).className = 'characterAbilityBoxSelected'
            }

        }
        else
        {
            alert('Selected Number of Cards = '+ selectedImages.length + ' Max Number of Cards allowed = '+maxCardsInHand);
        }

        if(selectedImages.length == maxCardsInHand && items_selected.length > 0)
        {
            document.getElementById('submitButton').disabled = false;
            document.getElementById("submitButton").className = 'PlayButtonEnabled'
        }
        else
        {
            document.getElementById('submitButton').disabled = true;
            document.getElementById("submitButton").className = 'PlayButtonDisabled'
        }
    }

    return <div id={props.characterCardId} className="characterAbilityBox" onClick={() => displayCharacterSelected()}>
    <img alt={''} className='tier2' src={props.charImg} />
    </div>
};

function goToApp(props) {

    ReactDOM.render(<App abilityCards={selectedImages} characterName={props.characterName} characterCardHand={props.characterCardHand} itemsSelected={items_selected} />, document.getElementById('root'));

}

class CharacterAbilityCardSelection extends Component{

  createCards=(name, hand) =>{
        let cards = [];
        let image = [];
        if(name == 'Brute') {
            image = BRUTE;
        }
        else{
            alert("Not ready for "+name)
        }

      maxCardsInHand = hand;
      const rows = image.length / 3;

        let index = 0;
      for(let i=0; i < rows; i++ )
      {
          let children = [];
          for(let j=0; j < 10 ; j++ )
          {
              if (index<image.length)
                  children.push(<CharacterAbilityBox characterCardId={image[index].id} charImg={image[index++].src}/>)
          }
          cards.push(<div style={{display:'flex',
                justifyContent:'space-evenly'}}>{children}</div>)
      }
    return cards
  };

    render = () => (
        <div className="CharacterAbilityCardSelection">

            <button hidden={true} onClick={() => window.location.reload(false)}> Back</button>
            <div style={{ textAlign:'center', display:'flex',
                justifyContent:'space-evenly'}}>
                <div className="BackButton"><img src={backImg} onClick={() => window.location.reload(false)}/></div>
                <h2>Select {this.props.characterCardHand} Cards in Hand for {this.props.characterName}</h2>
                <button id={'submitButton'} type={"button"} onClick={() => goToApp(this.props)}>Play!</button>
            </div>
            <div>{this.createCards(this.props.characterName, this.props.characterCardHand)}</div>
            <div>
            <ItemSelection items={items}/>
            </div>
        </div>
    );

    componentDidMount = () => (
        document.getElementById("submitButton").disabled = true,
        document.getElementById("submitButton").className = 'PlayButtonDisabled'

    )

}

export default CharacterAbilityCardSelection
