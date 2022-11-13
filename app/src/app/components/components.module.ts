import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core'
import { RouterModule } from '@angular/router'
import { CommonModule } from '@angular/common'

import { NavigationLinks } from './navigation-links/navigation-links.component'

@NgModule({
  declarations: [NavigationLinks],
  imports: [CommonModule, RouterModule],
  exports: [NavigationLinks],
  schemas: [CUSTOM_ELEMENTS_SCHEMA],
})
export class ComponentsModule {}
