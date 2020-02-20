import React, {Component} from 'react'
import App from './App';
import background from './characterImages/characterselectionbackground.jpg'
import spellweaver from './characterImages/spellweaver.jpg'
import brute from './characterImages/brute.jpg'
import beasttyrant from './characterImages/beast-tyrant.jpg'
import cragheart from './characterImages/cragheart.jpg'
import mindthief from './characterImages/mindthief.jpg'
import tinkerer from './characterImages/tinkerer.jpg'
import scoundrel from './characterImages/scoundrel.jpg'
import berserker from './characterImages/berserker.jpg'
import diviner from './characterImages/diviner.jpg'
import doomstalker from './characterImages/doomstalker.jpg'
import elementalist from './characterImages/elementalist.jpg'
import nightshroud from './characterImages/nightshroud.jpg'
import plagueherald from './characterImages/plagueherald.jpg'
import quartermaster from './characterImages/quartermaster.jpg'
import sawbone from './characterImages/sawbone.jpg'
import soothsinger from './characterImages/soothsinger.jpg'
import summoner from './characterImages/summoner.jpg'
import sunkeeper from './characterImages/sunkeeper.jpg'
import './CharacterSelect.css'
import ReactDOM from "react-dom";
import CharacterAbilityCardSelection from './characterAbilityCardSelection'


const CharacterBox = (props) => {

    function displayCharacterSelected() {
      ReactDOM.render(<CharacterAbilityCardSelection characterName={props.characterName} characterCardHand={props.characterCardHand}/>, document.getElementById('root'));
    }
    return <div className="characterBox">
    <h2>{props.characterName}</h2>
    <img alt={''} className='tier2' src={props.charImg} onClick={() => displayCharacterSelected()}/>
    </div>
}

const CharacterContainer = (props) =>{

        return(
            <div style={{display:'flex',
                justifyContent:'space-evenly'}}>
                   <CharacterBox
                       characterName={props.character1Name}
                       charImg={props.character1Image}
                       characterCardHand={props.character1CardHand}/>
                   <CharacterBox
                       characterName={props.character2Name}
                       charImg={props.character2Image}
                       characterCardHand={props.character2CardHand}/>
                   <CharacterBox
                       characterName={props.character3Name}
                       charImg={props.character3Image}
                       characterCardHand={props.character3CardHand}/>
                   <CharacterBox
                       characterName={props.character4Name}
                       charImg={props.character4Image}
                       characterCardHand={props.character4CardHand}/>
                   <CharacterBox
                       characterName={props.character5Name}
                       charImg={props.character5Image}
                       characterCardHand={props.character5CardHand}/>
                   <CharacterBox
                       characterName={props.character6Name}
                       charImg={props.character6Image}
                       characterCardHand={props.character6CardHand}/>
            </div>
        )
}

class GreyBox extends Component{
    render() {
        return(
            <div className='greyBox'>
                <CharacterContainer
                    character1Name={'Brute'}
                    character1Image={brute}
                    character1CardHand={10}
                    character2Name={'Cragheart'}
                    character2Image={cragheart}
                    character2CardHand={11}
                    character3Name={'Mindthief'}
                    character3Image={mindthief}
                    character3CardHand={10}
                    character4Name={'Scoundrel'}
                    character4Image={scoundrel}
                    character4CardHand={9}
                    character5Name={'Spellweaver'}
                    character5Image={spellweaver}
                    character5CardHand={8}
                    character6Name={'Tinkerer'}
                    character6Image={tinkerer}
                    character6CardHand={12}
                />
                <CharacterContainer
                    character1Name={'Beast Tyrant'}
                    character1Image={beasttyrant}
                    character1CardHand={10}
                    character2Name={'Berserker'}
                    character2Image={berserker}
                    character2CardHand={10}
                    character3Name={'Doomstalker'}
                    character3Image={doomstalker}
                    character3CardHand={12}
                    character4Name={'Elementalist'}
                    character4Image={elementalist}
                    character4CardHand={10}
                    character5Name={'Nightshroud'}
                    character5Image={nightshroud}
                    character5CardHand={9}
                    character6Name={'Plagueherald'}
                    character6Image={plagueherald}
                    character6CardHand={11}/>
                <CharacterContainer
                    character1Name={'Quartermaster'}
                    character1Image={quartermaster}
                    character1CardHand={9}
                    character2Name={'Sawbones'}
                    character2Image={sawbone}
                    character2CardHand={10}
                    character3Name={'Soothsinger'}
                    character3Image={soothsinger}
                    character3CardHand={9}
                    character4Name={'Summoner'}
                    character4Image={summoner}
                    character4CardHand={9}
                    character5Name={'Sunkeeper'}
                    character5Image={sunkeeper}
                    character5CardHand={11}
                    character6Name={'Diviner'}
                    character6Image={diviner}
                    character6CardHand={9}/>
            </div>
        )
    }
}

class CharacterSelect extends Component {

    render() {
        return (
            <div className="CharacterSelect" style={{backgroundImage: `url(${background})`}}>
                <h1 className='header'>Character Selection Screen</h1>
                <GreyBox/>
            </div>
        )
    }
}

export default CharacterSelect