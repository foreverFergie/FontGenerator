import { Component, OnInit, ChangeDetectionStrategy } from '@angular/core';

@Component({
  selector: 'app-list1',
  templateUrl: './list1.component.html',
  styleUrls: ['./list1.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class List1Component implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

}
