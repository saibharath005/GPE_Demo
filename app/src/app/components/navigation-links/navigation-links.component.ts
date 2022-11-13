import { Component, Input } from '@angular/core'

@Component({
  selector: 'navigation-links',
  templateUrl: 'navigation-links.component.html',
  styleUrls: ['navigation-links.component.css'],
})
export class NavigationLinks {
  @Input()
  DB: string = 'Dashboard'
  @Input()
  rootClassName: string = ''
  @Input()
  UM: string = 'User Management'
  @Input()
  AB: string = 'About'
  @Input()
  PM: string = 'Product Management'

  constructor() {}
}
