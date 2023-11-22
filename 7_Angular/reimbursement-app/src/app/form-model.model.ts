export class FormModel {
  constructor(
    public emp_id: string = '',
    public emp_name: string = '',
    public emp_designation: string = '',
    public reimbursement: ReimbursementModel[] = []
  ) {}
}

export class ReimbursementModel {
  constructor(
    public rname: string = '',
    public ramount: number = null,
    public type: string = ''
  ) {}
}
