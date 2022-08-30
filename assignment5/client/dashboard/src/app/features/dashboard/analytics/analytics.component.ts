import {
  ChangeDetectionStrategy,
  Component,
  OnDestroy,
  OnInit,
  ViewEncapsulation,
} from '@angular/core';
import { Router } from '@angular/router';
import { Subject, takeUntil } from 'rxjs';

import { DashboardService } from '../dashboard.service';

@Component({
  selector: 'analytics',
  templateUrl: './analytics.component.html',
  encapsulation: ViewEncapsulation.None,
})
export class AnalyticsComponent implements OnInit, OnDestroy {
  data: any;
  barChart1Data! :{x:string[],y:number[]}
  barChart2Data! :{x:string[],y:number[]}
  heatChart1Data! :{x:{'value':number,'name':string}[]};
  scatterChartData! :{x:{'value':number,'value1':number}[]};
  areaCharts = ['first', 'second', 'third', 'fourth'];
  private _unsubscribeAll: Subject<any> = new Subject<any>();

  /**
   * Constructor
   */
  constructor(
    private _dashboardService: DashboardService,
    private _router: Router
  ) {}

  // -----------------------------------------------------------------------------------------------------
  // @ Lifecycle hooks
  // -----------------------------------------------------------------------------------------------------

  /**
   * On init
   */
  async ngOnInit() {
    console.log('previous',this.barChart1Data)
    this._dashboardService.getBarChartOneDta().subscribe((res:any)=>{
      this.barChart1Data=res;
      console.log('barchart1datah',this.barChart1Data)
    })
    console.log('previous',this.barChart2Data)
    this._dashboardService.getBarChartTwoDta().subscribe((res:any)=>{
      this.barChart2Data=res;
      console.log('barchart2datah',this.barChart2Data)
    })
    console.log('previous',this.heatChart1Data)
    this._dashboardService.getHeatChartOneDta().subscribe((res:any)=>{
      this.heatChart1Data=res;
      console.log('heatchartdatah',this.heatChart1Data)
    })
    console.log('previous',this.scatterChartData)
    this._dashboardService.getScatterPlot().subscribe((res:any)=>{
      this.scatterChartData=res;
      console.log('scatterplot',this.scatterChartData)
    })
  }


  /**
   * On destroy
   */
  ngOnDestroy(): void {
    // Unsubscribe from all subscriptions
    this._unsubscribeAll.next(null);
    this._unsubscribeAll.complete();
  }

  // -----------------------------------------------------------------------------------------------------
  // @ Public methods
  // -----------------------------------------------------------------------------------------------------

  /**
   * Track by function for ngFor loops
   *
   * @param index
   * @param item
   */
  trackByFn(index: number, item: any): any {
    return item.id || index;
  }

  // -----------------------------------------------------------------------------------------------------
  // @ Private methods
  // -----------------------------------------------------------------------------------------------------

  /**
   *
   * @param element
   * @private
   */
}