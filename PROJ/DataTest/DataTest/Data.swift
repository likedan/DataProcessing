//
//  MazeParser.swift
//  440
//
//  Created by Wang Yu on 9/22/15.
//  Copyright © 2015 TakeFive Interactive. All rights reserved.
//

import Cocoa
import CoreData

let DataManager = Data()

class Data: NSObject {
    

    override init() {
        super.init()
        //parseTrainer()
        //print(getBidsList(fetchRequest))
    }
    
    func parseBids(){
        
        let paths = NSSearchPathForDirectoriesInDomains(.DocumentDirectory, .UserDomainMask, true) as NSArray
        let documentsDirectory = paths.objectAtIndex(0) as! NSString
        print(documentsDirectory)
        
        let path = NSBundle.mainBundle().pathForResource("bids", ofType: "csv")
        print(path)
        var text = ""
        do {
            text = try NSString(contentsOfFile: path!, encoding: NSUTF8StringEncoding) as String
        }
        catch {/* error handling here */}
        var lineArr = text.componentsSeparatedByString("\n")
        lineArr.removeFirst()
        var ind = 0;
        for line in lineArr{
            let arr = line.componentsSeparatedByString(",")
            saveData(arr)
            ind++
            if ind % 1000 == 0{
                print(ind)
            }
        }
        
    }
    

    
}

func saveData(var bids:[String]) {
    
    let paths = NSSearchPathForDirectoriesInDomains(.DocumentDirectory, .UserDomainMask, true) as NSArray
    let documentsDirectory = paths.objectAtIndex(0) as! NSString
    let path = documentsDirectory.stringByAppendingPathComponent("\(bids[1]).plist")
    
    let fileManager = NSFileManager.defaultManager()
    let bidID = bids[0]
    bids.removeFirst()
    bids.removeFirst()
    if(!fileManager.fileExistsAtPath(path)) {
        
        let dict = [bidID:bids]
        let diction = NSDictionary(dictionary: dict)
        diction.writeToFile(path, atomically: false)
    }else{
        let dict = NSMutableDictionary(contentsOfFile: path)
        dict?.setObject(bids, forKey: bidID)
        dict?.writeToFile(path, atomically: false)
    }

}

class BidData {
    
    var data:[String]
    
    init(data:String){
        self.data = data.componentsSeparatedByString(",")
    }
    
    lazy var bid_id:()->(String) = {
        return self.data[0]
    }
    lazy var bidder_id:()->(String) = {
        return self.data[1]
    }
    lazy var auction:()->(String) = {
        return self.data[2]
    }
    lazy var device:()->(String) = {
        return self.data[3]
    }
    lazy var merchandise:()->(String) = {
        return self.data[3]
    }
    lazy var time:()->(Int) = {
        return Int(self.data[5])!
    }
    lazy var country:()->(String) = {
        return self.data[6]
    }
    lazy var ip:()->(String) = {
        return self.data[7]
    }
    lazy var url:()->(String) = {
        return self.data[8]
    }
    
}