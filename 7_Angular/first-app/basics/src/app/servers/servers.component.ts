import { Component } from "@angular/core";

@Component({
    selector:"app-servers",
    templateUrl:"./servers.component.html",
    styleUrls:["./servers.component.css"]
})
export class ServersComponent{

    allowNewServers = false
    serverStatusString = "No server was created"
    serverName = ""
    serverCreated = false
    servers= ["Server 1", "Server 2", "Server 3"]

    constructor() {
        setTimeout(() => {
            this.allowNewServers = true;
        }, 2000);
    }  
    addNewServer(){
        this.serverCreated = true
        this.serverStatusString = `Server ${this.serverName} Created`
        this.servers.push(this.serverName)
    }

    getServerName(event: any){
        this.serverName = event.target.value
    }

}