//
//  dsdfsdfViewController.swift
//  412test
//
//  Created by Kedan Li on 15/9/19.
//  Copyright © 2015年 TakeFive Interactive. All rights reserved.
//

import UIKit

class dsdfsdfViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        let path = NSBundle.mainBundle().pathForResource("vectors", ofType: "txt")
        print(path)
        var text = ""
        do {
            text = try NSString(contentsOfFile: path!, encoding: NSUTF8StringEncoding) as String
            //print(text)
        }
        catch {/* error handling here */}
        let lineArr = text.componentsSeparatedByString("\n")
        let arr1 = lineArr[0].componentsSeparatedByString("\t")
        let arr2 = lineArr[1].componentsSeparatedByString("\t")

        var total = 0
        
        for var index = 0; index < arr1.count; index++ {
            total = total + (Int(arr1[index])! - Int(arr2[index])!) * (Int(arr1[index])! - Int(arr2[index])!)
        }
        let h2 = sqrt(Double(total))
        print(h2)
        
        total = 0
        
        for var index = 0; index < arr1.count; index++ {
            total = total + abs((Int(arr1[index])! - Int(arr2[index])!) * (Int(arr1[index])! - Int(arr2[index])!) * (Int(arr1[index])! - Int(arr2[index])!))
        }
        
        let h3 = cbrt(Double(total))
        print(h3)
        // Do any additional setup after loading the view.
    }

}
