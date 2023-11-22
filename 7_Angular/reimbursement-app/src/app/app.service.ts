import { Injectable } from '@angular/core';

import { Subject } from 'rxjs';

import { FormModel, ReimbursementModel } from './form-model.model';

@Injectable()
export class FormService {
  inputForms: FormModel = new FormModel('', '', '', [
    new ReimbursementModel('', null, ''),
  ]);
  newFormEvent = new Subject<boolean>();

  getForms() {
    return JSON.parse(JSON.stringify(this.inputForms));
  }
  addForm(forms: FormModel) {
    this.inputForms = forms;
    this.newFormEvent.next(true);
  }
}
