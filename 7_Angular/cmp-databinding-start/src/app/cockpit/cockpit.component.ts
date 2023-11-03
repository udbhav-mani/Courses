import { Component, ElementRef, EventEmitter, Output, ViewChild } from '@angular/core';

@Component({
  selector: 'app-cockpit',
  templateUrl: './cockpit.component.html',
//   styleUrls: ['./cockpit.component.css']
})
export class CockpitComponent {  

  @ViewChild("newServerContent", {static: true}) newServerContent:ElementRef;
  @Output("serverCreationEvent") serverCreated = new EventEmitter<{serverName:string, serverContent:string}>();
  @Output("bpCreationEvent") blueprintCreated = new EventEmitter<{serverName:string, serverContent:string}>();

  onAddServer(newServerName:HTMLInputElement) {
    this.serverCreated.emit({
        serverName:newServerName.value,
        serverContent:this.newServerContent.nativeElement.value
    })
  }

  onAddBlueprint(newServerName:HTMLInputElement) {
    this.blueprintCreated.emit({
        serverName:newServerName.value,
        serverContent:this.newServerContent.nativeElement.value
    })
  }

}
