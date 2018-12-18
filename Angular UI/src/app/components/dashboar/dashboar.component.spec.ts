import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DashboarComponent } from './dashboar.component';

describe('DashboarComponent', () => {
  let component: DashboarComponent;
  let fixture: ComponentFixture<DashboarComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DashboarComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DashboarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
