import { Component, OnInit, Input } from '@angular/core';
import { dataTool, EChartsOption } from 'echarts';
import { DashboardService } from 'src/app/features/dashboard/dashboard.service';

@Component({
  selector: 'app-heat-chart',
  templateUrl: './heatmap-chart.component.html',
  styleUrls: ['./heatmap-chart.component.scss'],
})
export class HeatMapChartComponent implements OnInit {
  @Input() chartUrl = '';
  @Input() chartData :any;
  _chartOption: EChartsOption = {};

  constructor(private dashser:DashboardService) {

  }

  ngOnInit() {
    this.loadChart(this.chartData['x'])
  }

  private loadChart(data: any): void {

    const hours = [
      '12a', '1a', '2a', '4a', '5a', '6a','10a'

    ];

    // prettier-ignore
    const days = [
      'Daily Oil Consume', 'Yearly Gallon Per Capita', 'Price Per Gallon',
      'Price Per Liter', 'GDP Per Capita', 'Gallons GDP Per Capita Can Buy', 'Yearly Gallons Per Capita Buy'
    ];


    this._chartOption = {
      tooltip: {
        position: 'top'
      },
      grid: {
        height: '50%',
        width: '50%',
        right:'20%',
        top: '10%'
      },
      xAxis: {
        type: 'category',
        data: hours,
        splitArea: {
          show: true
        }
      },
      yAxis: {
        type: 'category',
        data: days,
        splitArea: {
          show: true
        }
      },
      visualMap: {
        min: -0.1,
        max: 1,
        calculable: true,
        orient: 'horizontal',
        left: 'center',
        bottom: '15%'
      },
      series: [
        {
          name: 'Punch Card',
          type: 'heatmap',
          data: data,
          label: {
            show: true
          },
          emphasis: {
            itemStyle: {
              shadowBlur: 10,
              shadowColor: 'rgba(255, 0, 0, 0.8)'
            }
          }
        }
      ]
    };
  }
}