import { Component, Input } from '@angular/core';
import { UserServiceComponent } from '../shared/users.service';

@Component({
  selector: 'app-inactive-users',
  templateUrl: './inactive-users.component.html',
  styleUrls: ['./inactive-users.component.css'],
})
export class InactiveUsersComponent {
  users: string[] = [];
  constructor(private userService: UserServiceComponent) {}

  ngOnInit() {
    this.users = this.userService.inactiveUsers;
  }

  onSetToActive(id: number) {
    this.userService.onSetToActive(id);
  }
}
