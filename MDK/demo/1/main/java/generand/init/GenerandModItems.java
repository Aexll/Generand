
/*
 *    MCreator note: This file will be REGENERATED on each build.
 */
package generand.init;

import net.minecraftforge.registries.RegistryObject;
import net.minecraftforge.registries.ForgeRegistries;
import net.minecraftforge.registries.DeferredRegister;

import net.minecraft.world.level.block.Block;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.CreativeModeTab;
import generand.GenerandMod;
import generand.item.TestItemItem;
import net.minecraft.world.item.BlockItem;

public class GenerandModItems {
	public static final DeferredRegister<Item> REGISTRY = DeferredRegister.create(ForgeRegistries.ITEMS, GenerandMod.MODID);
	public static final RegistryObject<Item> TEST_ITEM = REGISTRY.register("test_item", () -> new TestItemItem());
	public static final RegistryObject<Item> TEST_ORE = block(GenerandModBlocks.TEST_ORE, CreativeModeTab.TAB_BUILDING_BLOCKS);

	private static RegistryObject<Item> block(RegistryObject<Block> block, CreativeModeTab tab) {
		return REGISTRY.register(block.getId().getPath(), () -> new BlockItem(block.get(), new Item.Properties().tab(tab)));
	}
}
