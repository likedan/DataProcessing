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
            finalScore.insert(Int(strArr[1])!, atIndex: lineArr.indexOf(line)!)
        }
        
        finalScore = mergeSort(finalScore)

        var mean:Double = 0;
        
        for score in finalScore {
            mean = mean + Double(score)
        }
        mean = mean / Double(finalScore.count)
        
        print(mean)
        
        var empiricalVar:Double = 0
        for score in finalScore {
            empiricalVar = empiricalVar + (mean - Double(score)) * (mean - Double(score))
        }
        empiricalVar = empiricalVar / Double(finalScore.count - 1)
        print(empiricalVar)
        
        var s:Double = sqrt(empiricalVar)
        /*for score in finalScore {
            s = s + abs(mean - Double(score))
        }
        s = s / Double(finalScore.count)*/
        print(s)
        
        var zValues = [Double]()

        for score in finalScore {
            zValues.append((Double(score) - mean)/s)
        }
        print((90 - mean)/s)
        var zmean:Double = 0;
        for z in zValues {
            zmean = zmean + z
        }
        zmean = zmean / Double(zValues.count)
        print(zmean)
        
        
        print(zmean/Double(finalScore.count))

        empiricalVar = 0
        for score in zValues {
            empiricalVar = empiricalVar + score * score
        }
        empiricalVar = empiricalVar / Double(zValues.count - 1)
        print(empiricalVar)
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

