import { Component } from "@angular/core";

@Component({
    selector:"app-server",
    templateUrl:"./server.component.html",
    styles:[`
    .online{
        color:white;
    }
    `]
})
export class ServerComponent{
    serverId = 1;
    serverStatus:string = "offline";

    constructor() {
        this.serverStatus = Math.random() > 0.5?"offline":"online"        
    }  

    getColor(){
        return this.serverStatus==="offline"?"red":"green"
    }

}