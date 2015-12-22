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
        let path = NSBundle.mainBundle().pathForResource("data", ofType: "txt")
        print(path)
         var text = ""
        do {
           text = try NSString(contentsOfFile: path!, encoding: NSUTF8StringEncoding) as String
            //print(text)
        }
        catch {/* error handling here */}
        
        var finalScore = [Int]()
        let lineArr = text.componentsSeparatedByString("\n")
        for line in lineArr {
            let strArr = line.componentsSeparatedByString("\t")
            finalScore.insert(Int(strArr[2])!, atIndex: lineArr.indexOf(line)!)
        }
        
        finalScore = mergeSort(finalScore)
        
        let Q1: Double = Double((finalScore[finalScore.count / 4 - 1] + finalScore[finalScore.count / 4])) / 2
        let median: Double = Double((finalScore[finalScore.count / 2 - 1] + finalScore[finalScore.count / 2])) / 2
        let Q3: Double = Double((finalScore[finalScore.count / 4 * 3 - 1] + finalScore[finalScore.count / 4 * 3])) / 2.0

        var mean:Double = 0;
        
        for score in finalScore {
            mean = mean + Double(score)
        }
        mean = mean / Double(finalScore.count)
        
        print(Q1)
        print(median)
        print(Q3)
        print(mean)
        
        var modeChecker = [String: Int]()
        for score in finalScore {
            if modeChecker["\(score)"] == nil{
                modeChecker["\(score)"] = 1
            }else{
                modeChecker["\(score)"] = modeChecker["\(score)"]! + 1
            }
        }
        var highest = 0
        var highestKey = ""
        for key in Array(modeChecker.keys) {
            if modeChecker[key] > highest {
                highest = modeChecker[key]!
                highestKey = key
            }
        }
        print(highestKey)
        
        // setup the graph
        
        let size = CGFloat(finalScore.maxElement()! - finalScore.minElement()!)
        
        let plotView = UIView(frame: CGRectMake(0, 0, size * 3, 200))
        self.view.addSubview(plotView)
        for key in Array(modeChecker.keys) {
            
            let lineView = UIView(frame: CGRectMake(CGFloat(Int(key)!) * 3, 200 - CGFloat(modeChecker[key]! * 2), 2, CGFloat(modeChecker[key]! * 2)))
            lineView.backgroundColor = UIColor.blueColor()
            plotView.addSubview(lineView)
            
        }
        
    }
    
    func merge(var list1: [Int], var list2:[Int])->[Int]{
        
        var list = [Int]()
        
        while list1.count > 0 || list2.count > 0{
            if list1.count == 0{
                return list + list2
            }else if list2.count == 0{
                return list + list1
            }else{
                if list1[0] > list2[0]{
                    list.append(list2[0])
                    list2.removeAtIndex(0)
                }else{
                    list.append(list1[0])
                    list1.removeAtIndex(0)
                }
            }
        }
        
        return list
    }
    
    func mergeSort(var theList:[Int])->[Int]{
        if theList.count >= 2{
            let list1 = theList[0...(theList.count / 2 - 1)]
            let list2 = theList[(theList.count / 2)...(theList.count - 1)]
            return merge(mergeSort(Array(list1)), list2: mergeSort(Array(list2)))
        }
        return theList
    }
    

}

