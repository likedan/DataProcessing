//
//  ViewController.swift
//  412test
//
//  Created by Kedan Li on 15/9/18.
//  Copyright © 2015年 TakeFive Interactive. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        let path = NSBundle.mainBundle().pathForResource("Data-Q2", ofType: "txt")
         var text = ""
        do {
           text = try NSString(contentsOfFile: path!, encoding: NSUTF8StringEncoding) as String
        }
        catch {/* error handling here */}
        
        var data = [[String]]()
        let lineArr = text.componentsSeparatedByString("\n")
        for line in lineArr {
            let strArr = line.componentsSeparatedByString("\t")
            data.append(strArr)
        }
        
        print(data)
        
        //part B
        var distinct = [String:[String:[String:[String: Int]]]]()
        
        for elem in data{
            let city = elem[1]
            let category = elem[3]
            let price = elem[4]
            let time = elem[6]
            if distinct[city] == nil{
                distinct.updateValue([String:[String:[String: Int]]](), forKey: city)
                distinct[city]!.updateValue([String:[String: Int]](), forKey: category)
                distinct[city]![category]!.updateValue([String: Int](), forKey: price)
                distinct[city]![category]![price]!.updateValue(1, forKey: time)
            }else{
                if distinct[city]![category] == nil{
                    distinct[city]!.updateValue([String:[String: Int]](), forKey: category)
                    distinct[city]![category]!.updateValue([String: Int](), forKey: price)
                    distinct[city]![category]![price]!.updateValue(1, forKey: time)
                }else{
                    if distinct[city]![category]![price] == nil{
                        distinct[city]![category]!.updateValue([String: Int](), forKey: price)
                        distinct[city]![category]![price]!.updateValue(1, forKey: time)
                    }else{
                        if distinct[city]![category]![price]![time] == nil{
                            distinct[city]![category]![price]!.updateValue(1, forKey: time)
                        }else{
                            distinct[city]![category]![price]!.updateValue( distinct[city]![category]![price]![time]! + 1, forKey: time)
                        }
                    }
                }
            }
        }
        
        var count = 0
        for city in Array(distinct.keys){
            for category in Array(distinct[city]!.keys){
                for price in Array(distinct[city]![category]!.keys){
                    for time in Array(distinct[city]![category]![price]!.keys){
                        count++
                    }
                }
            }
        }
        
        print(count)
        
        //part C
        distinct = [String:[String:[String:[String: Int]]]]()
        count = 0
        
        for elem in data{
            let state = elem[2]
            let category = elem[3]
            let price = elem[4]
            let time = elem[6]
            if distinct[state] == nil{
                distinct.updateValue([String:[String:[String: Int]]](), forKey: state)
                distinct[state]!.updateValue([String:[String: Int]](), forKey: category)
                distinct[state]![category]!.updateValue([String: Int](), forKey: price)
                distinct[state]![category]![price]!.updateValue(1, forKey: time)
            }else{
                if distinct[state]![category] == nil{
                    distinct[state]!.updateValue([String:[String: Int]](), forKey: category)
                    distinct[state]![category]!.updateValue([String: Int](), forKey: price)
                    distinct[state]![category]![price]!.updateValue(1, forKey: time)
                }else{
                    if distinct[state]![category]![price] == nil{
                        distinct[state]![category]!.updateValue([String: Int](), forKey: price)
                        distinct[state]![category]![price]!.updateValue(1, forKey: time)
                    }else{
                        if distinct[state]![category]![price]![time] == nil{
                            distinct[state]![category]![price]!.updateValue(1, forKey: time)
                        }else{
                            distinct[state]![category]![price]!.updateValue( distinct[state]![category]![price]![time]! + 1, forKey: time)
                        }
                    }
                }
            }
        }
        
        for state in Array(distinct.keys){
            for category in Array(distinct[state]!.keys){
                for price in Array(distinct[state]![category]!.keys){
                    for time in Array(distinct[state]![category]![price]!.keys){
                        count++
                    }
                }
            }
        }
        print(count)

        //part D
        distinct = [String:[String:[String:[String: Int]]]]()
        
        for elem in data{
            let category = elem[3]
            let price = elem[4]
            let time = elem[5]
            if distinct[time] == nil{
                distinct.updateValue([String:[String:[String: Int]]](), forKey: time)
                distinct[time]!.updateValue([String:[String: Int]](), forKey: category)
                distinct[time]![category]!.updateValue([String: Int](), forKey: price)
                distinct[time]![category]![price]!.updateValue(1, forKey: elem[0])
                distinct[time]![category]![price]!.updateValue(1, forKey: elem[1])
                distinct[time]![category]![price]!.updateValue(1, forKey: elem[2])
                distinct[time]![category]![price]!.updateValue(1, forKey: elem[6])
            }else{
                if distinct[time]![category] == nil{
                    distinct[time]!.updateValue([String:[String: Int]](), forKey: category)
                    distinct[time]![category]!.updateValue([String: Int](), forKey: price)
                    distinct[time]![category]![price]!.updateValue(1, forKey: elem[0])
                    distinct[time]![category]![price]!.updateValue(1, forKey: elem[1])
                    distinct[time]![category]![price]!.updateValue(1, forKey: elem[2])
                    distinct[time]![category]![price]!.updateValue(1, forKey: elem[6])
                    
                }else{
                    if distinct[time]![category]![price] == nil{
                        distinct[time]![category]!.updateValue([String: Int](), forKey: price)
                        distinct[time]![category]![price]!.updateValue(1, forKey: elem[0])
                        distinct[time]![category]![price]!.updateValue(1, forKey: elem[1])
                        distinct[time]![category]![price]!.updateValue(1, forKey: elem[2])
                        distinct[time]![category]![price]!.updateValue(1, forKey: elem[6])
                        
                    }else{
                        
                    }
                }
            }
        }

        count = 0
        for time in Array(distinct.keys){
            for category in Array(distinct[time]!.keys){
                for price in Array(distinct[time]![category]!.keys){
                    for other in Array(distinct[time]![category]![price]!.keys){
                        count++
                    }
                }
            }
        }
        count = count / 4
        print(count)
      
        //part E
        
        count = 0
        var distinct2 = [String: Int]()
        for elem in data{
            let category = elem[3]
            let state = elem[2]
            let time = elem[5]
            if category == "food" && state == "Illinois" && time == "Q1" {

                distinct2.updateValue(1, forKey: elem[0])
                distinct2.updateValue(1, forKey: elem[1])
                distinct2.updateValue(1, forKey: elem[4])
                distinct2.updateValue(1, forKey: elem[6])
            }
            
        }
        
        for other in Array(distinct2.keys){
            count++
        }
        print(count)
        
        //part F
        
        count = 0
        distinct2 = [String: Int]()
        for elem in data{
            let price = elem[4]
            let city = elem[1]
            let time = elem[6]
            if price == "cheap" && city == "Chicago" && time == "2013" {
                
                distinct2.updateValue(1, forKey: elem[0])
                distinct2.updateValue(1, forKey: elem[1])
                distinct2.updateValue(1, forKey: elem[3])
                distinct2.updateValue(1, forKey: elem[5])
            }
            
        }
        
        for other in Array(distinct2.keys){
            count++
        }
        print(count)
        //(Location[City] = Chicago, *, Price = cheap,   Time[Year]= 2013)
    
    }
    
}

