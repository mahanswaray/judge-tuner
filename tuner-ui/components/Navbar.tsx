import {
  NavigationMenu,
  NavigationMenuContent,
  NavigationMenuIndicator,
  NavigationMenuItem,
  NavigationMenuLink,
  NavigationMenuList,
  NavigationMenuTrigger,
  NavigationMenuViewport,
  navigationMenuTriggerStyle
} from "@/components/ui/navigation-menu"
import { RefreshCw } from "lucide-react"

import Link from "next/link"
import { Button } from "./ui/button"


export default function Navbar() {

  return (
    <NavigationMenu className="w-full">
      <NavigationMenuList className="w-full justify-between">
        <div className="flex">
          <NavigationMenuItem>
            <Link href="/main" legacyBehavior passHref>
              <NavigationMenuLink className={navigationMenuTriggerStyle()}>
                Main
              </NavigationMenuLink>
            </Link>
          </NavigationMenuItem>
          <NavigationMenuItem>
            <Link href="/view" legacyBehavior passHref>
              <NavigationMenuLink className={navigationMenuTriggerStyle()}>
                Config
              </NavigationMenuLink>
            </Link>
          </NavigationMenuItem>
        </div>
        <NavigationMenuItem className="pl-[80vw]">
          <NavigationMenuLink>
            <Button className="bg-black hover:bg-gray-800">
              <div className="flex gap-2 items-center">
                <RefreshCw size={16} />
                <p>
                  Run Tests
                </p>
              </div>
            </Button>
          </NavigationMenuLink>

        </NavigationMenuItem>
      </NavigationMenuList>
    </NavigationMenu>
  )
}