import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-dashboar',
  templateUrl: './dashboar.component.html',
  styleUrls: ['./dashboar.component.scss']
})
export class DashboarComponent implements OnInit {
  loading:any
  constructor() { }

  ngOnInit() {
    this.loading = 2
  }
  ngAfterViewInit() {
      this.loading = 1
    // console.log("ff")
  }
}
