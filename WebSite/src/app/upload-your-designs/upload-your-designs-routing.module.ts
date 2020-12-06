import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { UploadYourDesignsComponent } from './upload-your-designs.component';

const routes: Routes = [
  { path: '', component: UploadYourDesignsComponent },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class UploadYourDesignsRoutingModule { }
