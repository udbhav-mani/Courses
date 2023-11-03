import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  oddNumbers:number[] = []
  evenNumbers:number[] = []

  logGame(gameEvent: {count:number}){
    if(gameEvent.count %2 == 1){
      this.oddNumbers.push(gameEvent.count)
    }
    else{
      this.evenNumbers.push(gameEvent.count)
    }
  }
}
