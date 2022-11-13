import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core'
import { RouterModule } from '@angular/router'
import { CommonModule } from '@angular/common'

import { ComponentsModule } from '../../components/components.module'
import { Welcome } from './welcome.component'

const routes = [
  {
    path: '',
    component: Welcome,
  },
]

@NgModule({
  declarations: [Welcome],
  imports: [CommonModule, ComponentsModule, RouterModule.forChild(routes)],
  exports: [Welcome],
  schemas: [CUSTOM_ELEMENTS_SCHEMA],
})
export class WelcomeModule {}
