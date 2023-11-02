import { Component } from "@angular/core";
@Component({
    selector:"password",
    templateUrl:"./password.component.html",
    styles:[`
    .more {
        color:white
    }

    `]
})
export class PasswordComponent{
    isDisplayed:boolean = false
    logs = []
    isAdmin:string = "admin"
    name:string = "dfhgsfj"
    name2:string = "hello"

    displayDetails(){
        // this.name = e.target.value
    }
    getInput(e){
        this.name = e.target.value
    }

}