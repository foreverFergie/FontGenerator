import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { UploadYourDesignsRoutingModule } from './upload-your-designs-routing.module';
import { UploadYourDesignsComponent } from './upload-your-designs.component';
import { ListComponent } from './list/list.component';
import { List1Component } from './list1/list1.component';
import { SharedModule } from '../shared/shared.module';


@NgModule({
  declarations: [UploadYourDesignsComponent, ListComponent, List1Component],
  imports: [
    CommonModule,
    UploadYourDesignsRoutingModule,
    SharedModule
  ]
})
export class UploadYourDesignsModule { }
