import { Component, EventEmitter, Output } from "@angular/core";
@Component({
    selector:"app-game-control",
    templateUrl:"./game-control.component.html",
})
export class GameControlComponent{
    @Output('gameEvent') gameEvent = new EventEmitter()
    count:number = 1
    intervalId:any
    


    startGame(){
        this.intervalId = setInterval(()=>{
            this.gameEvent.emit({count:this.count})
            this.count++;
        }, 1000)
    }

    endGame(){
        clearInterval(this.intervalId)
    }
    

}