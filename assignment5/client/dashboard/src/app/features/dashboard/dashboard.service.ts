import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject, Observable, tap } from 'rxjs';
import { ActivatedRoute, Router } from '@angular/router';

@Injectable({
  providedIn: 'root',
})
export class DashboardService {

  /**
   * Constructor
   */
  constructor(private _httpClient: HttpClient,private router:Router,private ar:ActivatedRoute) {}

  // -----------------------------------------------------------------------------------------------------
  // @ Accessors
  // -----------------------------------------------------------------------------------------------------

  // -----------------------------------------------------------------------------------------------------
  // @ Public methods
  // -----------------------------------------------------------------------------------------------------


  getBarChartOneDta():Observable<any>{
    console.log('BarChart1')
    return this._httpClient.get<{x:string[],y:number[]}>('http://localhost:5000/barchartone');
  }
  getBarChartTwoDta():Observable<any>{
    console.log('BarChart2')
    return this._httpClient.get<{x:string[],y:number[]}>('http://localhost:5000/barcharttwo');
  }
  getHeatChartOneDta():Observable<any>{
    console.log('HeatMap')
    return this._httpClient.get<{x:{'value':number,'name':string}[]}>('http://localhost:5000/histogramchart');
  }
  getScatterPlot():Observable<any>{
    console.log('Scatter Chart')
    return this._httpClient.get<{x:{'value':number,'name':string}[]}>('http://localhost:5000/scatterchart');
  }

}