#!/usr/bin/env python3
"""
🤖 Bazar da Thaís - Auto Photo Processing
Monitora pasta photos/to_process e processa automaticamente novas fotos
"""
import os
import time
import json
import shutil
from datetime import datetime
from pathlib import Path
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('data/processing_logs.log'),
        logging.StreamHandler()
    ]
)

class AutoPhotoProcessor:
    def __init__(self):
        self.base_path = Path(__file__).parent.parent
        self.to_process = self.base_path / "photos" / "to_process"
        self.processed = self.base_path / "photos" / "processed" 
        self.failed = self.base_path / "photos" / "failed"
        self.data_file = self.base_path / "data" / "produtos_bazar.json"
        self.logs_file = self.base_path / "data" / "processing_logs.json"
        
        # Supported image extensions
        self.image_extensions = {'.jpg', '.jpeg', '.png', '.webp', '.heic', '.bmp', '.tiff'}
        
        # Ensure directories exist
        for path in [self.to_process, self.processed, self.failed]:
            path.mkdir(parents=True, exist_ok=True)
            
    def log_processing(self, filename, status, product_data=None, error=None):
        """Log processing results"""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "filename": filename,
            "status": status,  # success, failed, low_confidence
            "product_data": product_data,
            "error": str(error) if error else None
        }
        
        try:
            # Read existing logs
            if self.logs_file.exists():
                with open(self.logs_file, 'r', encoding='utf-8') as f:
                    logs = json.load(f)
            else:
                logs = []
                
            # Add new log
            logs.append(log_entry)
            
            # Keep only last 1000 logs
            if len(logs) > 1000:
                logs = logs[-1000:]
                
            # Save logs
            with open(self.logs_file, 'w', encoding='utf-8') as f:
                json.dump(logs, f, indent=2, ensure_ascii=False)
                
        except Exception as e:
            logging.error(f"Failed to log processing: {e}")
    
    def detect_makeup_products(self, image_path):
        """
        Enhanced AI detection for MULTIPLE products in one image
        Returns list of products found in the image
        """
        try:
            filename = os.path.basename(image_path).lower()
            
            # Enhanced mock detection for multiple products
            # In production, this would use actual AI vision API with multi-object detection
            
            # Simulate different scenarios based on filename patterns
            if any(word in filename for word in ['collection', 'haul', 'flatlay', 'multiple', 'set', 'kit']):
                # Multi-product scenarios
                mock_products = [
                    {
                        "marca": "Fenty Beauty",
                        "produto": "Pro Filt'r Foundation",
                        "cor_tom": "350",
                        "tipo": "Base",
                        "volume": "32ml",
                        "confidence": 88,
                        "brand_category": "premium",
                        "product_type": "medium_risk",
                        "condition": "novo",
                        "position": "left side"
                    },
                    {
                        "marca": "Fenty Beauty", 
                        "produto": "Match Stix Concealer",
                        "cor_tom": "350",
                        "tipo": "Corretivo", 
                        "volume": "8ml",
                        "confidence": 85,
                        "brand_category": "premium",
                        "product_type": "medium_risk",
                        "condition": "25_usado",
                        "position": "center"
                    },
                    {
                        "marca": "Fenty Beauty",
                        "produto": "Killawatt Highlighter", 
                        "cor_tom": "Trophy Wife",
                        "tipo": "Iluminador",
                        "volume": "8g",
                        "confidence": 82,
                        "brand_category": "premium", 
                        "product_type": "low_risk",
                        "condition": "50_usado",
                        "position": "right side"
                    }
                ]
            elif any(word in filename for word in ['lipstick', 'lip', 'batom']):
                # Lipstick collection scenario
                lipstick_shades = [
                    ("Pillow Talk", "3.5g", 92, "ultra_premium"),
                    ("Very Victoria", "3.5g", 89, "ultra_premium"), 
                    ("Walk of No Shame", "3.5g", 87, "ultra_premium")
                ]
                
                mock_products = []
                for i, (shade, volume, confidence, category) in enumerate(lipstick_shades):
                    mock_products.append({
                        "marca": "Charlotte Tilbury",
                        "produto": "Matte Revolution Lipstick",
                        "cor_tom": shade,
                        "tipo": "Batom",
                        "volume": volume,
                        "confidence": confidence,
                        "brand_category": category,
                        "product_type": "high_risk",
                        "condition": "novo" if i == 0 else "25_usado",
                        "position": f"position {i+1}"
                    })
            else:
                # Single product (existing logic)
                single_products = [
                    {
                        "marca": "Urban Decay",
                        "produto": "Naked Heat Eyeshadow Palette",
                        "cor_tom": "Multi",
                        "tipo": "Paleta de Sombras",
                        "volume": "15.6g",
                        "confidence": 78,
                        "brand_category": "premium", 
                        "product_type": "low_risk",
                        "condition": "50_usado",
                        "position": "single"
                    }
                ]
                
                # Sometimes return multiple even for "single" photos
                import random
                if random.random() < 0.3:  # 30% chance of finding multiple products
                    single_products.append({
                        "marca": "Urban Decay",
                        "produto": "Eyeshadow Primer Potion",
                        "cor_tom": "Original",
                        "tipo": "Primer",
                        "volume": "10ml", 
                        "confidence": 75,
                        "brand_category": "premium",
                        "product_type": "medium_risk",
                        "condition": "usado_25",
                        "position": "background"
                    })
                
                mock_products = single_products
            
            # Filter by confidence threshold
            valid_products = [p for p in mock_products if p.get("confidence", 0) >= 60]
            
            logging.info(f"🔍 Detected {len(valid_products)} products in {filename}")
            return valid_products
            
        except Exception as e:
            logging.error(f"AI detection failed for {image_path}: {e}")
            return []
    
    def research_market_prices(self, product_data):
        """
        Mock market research function
        In production, would scrape actual store prices
        """
        try:
            # Mock pricing based on brand category
            base_prices = {
                "ultra_premium": {"min": 180, "max": 250, "median": 215},
                "premium": {"min": 120, "max": 180, "median": 150},
                "mid": {"min": 60, "max": 120, "median": 90},
                "nacional": {"min": 30, "max": 80, "median": 55},
                "drugstore": {"min": 15, "max": 50, "median": 32}
            }
            
            category = product_data.get("brand_category", "mid")
            prices = base_prices.get(category, base_prices["mid"])
            
            return {
                "min_price": prices["min"],
                "max_price": prices["max"], 
                "median": prices["median"],
                "average": (prices["min"] + prices["max"]) / 2,
                "sources": 8,
                "research_date": datetime.now().strftime("%Y-%m-%d")
            }
            
        except Exception as e:
            logging.error(f"Market research failed: {e}")
            return None
    
    def calculate_bazar_prices(self, product_data, market_data):
        """Calculate 4-tier bazar pricing"""
        try:
            min_price = market_data["min_price"]
            median = market_data["median"]
            
            # Brand adjustments
            brand_adjustments = {
                "ultra_premium": -0.05,
                "premium": -0.03, 
                "mid": 0.00,
                "nacional": 0.00,
                "drugstore": 0.05
            }
            
            # Risk adjustments
            risk_adjustments = {
                "high_risk": -0.18,
                "medium_risk": -0.05,
                "low_risk": 0.00
            }
            
            brand_adj = brand_adjustments.get(product_data.get("brand_category", "mid"), 0)
            risk_adj = risk_adjustments.get(product_data.get("product_type", "low_risk"), 0)
            total_adjustment = brand_adj + risk_adj
            
            # Base calculations
            base_prices = {
                "nunca_usado": min_price * 0.75,
                "usado_25": median * 0.60,
                "usado_50": median * 0.45,
                "usado_75": median * 0.30
            }
            
            # Apply adjustments
            final_prices = {}
            for condition, price in base_prices.items():
                adjusted_price = max(price * (1 + total_adjustment), 5.0)
                final_prices[condition] = round(adjusted_price, 2)
            
            return final_prices
            
        except Exception as e:
            logging.error(f"Price calculation failed: {e}")
            return None
    
    def add_to_database(self, product_data, market_data, calculated_prices):
        """Add processed product to database"""
        try:
            # Load existing data
            if self.data_file.exists():
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    products = json.load(f)
            else:
                products = []
            
            # Get next ID
            next_id = max([p.get('id', 0) for p in products], default=0) + 1
            
            # Create new product entry
            new_product = {
                "id": next_id,
                "marca": product_data["marca"],
                "produto": product_data["produto"],
                "cor_tom": product_data["cor_tom"],
                "tipo": product_data["tipo"],
                "volume": product_data["volume"],
                "categoria_risco": product_data["product_type"],
                "preco_min": market_data["min_price"],
                "preco_max": market_data["max_price"],
                "preco_medio": market_data["average"],
                "mediana": market_data["median"],
                "fontes": market_data["sources"],
                "data_pesquisa": market_data["research_date"],
                "ajuste_categoria": product_data["brand_category"],
                "nunca_usado": calculated_prices["nunca_usado"],
                "usado_25": calculated_prices["usado_25"],
                "usado_50": calculated_prices["usado_50"],
                "usado_75": calculated_prices["usado_75"],
                "observacoes": f"Processado automaticamente - Confiança: {product_data['confidence']}%",
                "auto_processed": True,
                "processed_timestamp": datetime.now().isoformat()
            }
            
            # Add to products
            products.append(new_product)
            
            # Save updated database
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(products, f, indent=2, ensure_ascii=False)
            
            logging.info(f"✅ Product {next_id} added: {product_data['marca']} {product_data['produto']}")
            return new_product
            
        except Exception as e:
            logging.error(f"Failed to add to database: {e}")
            return None
    
    def process_single_photo(self, photo_path):
        """Process a single photo that may contain MULTIPLE products"""
        filename = os.path.basename(photo_path)
        
        try:
            logging.info(f"🔄 Processing {filename}...")
            
            # Step 1: AI Detection (now returns list of products)
            products_detected = self.detect_makeup_products(photo_path)
            if not products_detected:
                raise Exception("No products detected in image")
                
            successful_products = []
            failed_products = []
            
            # Process each detected product
            for i, product_data in enumerate(products_detected):
                product_position = product_data.get('position', f'product_{i+1}')
                
                try:
                    logging.info(f"  🔍 Processing product {i+1}/{len(products_detected)}: {product_data['marca']} {product_data['produto']}")
                    
                    # Step 2: Confidence check per product
                    if product_data.get("confidence", 0) < 70:
                        logging.warning(f"  ❌ Low confidence ({product_data['confidence']}%) for {product_data['produto']}")
                        failed_products.append({
                            "product": product_data,
                            "reason": f"Low confidence ({product_data['confidence']}%)"
                        })
                        continue
                    
                    # Step 3: Market research
                    market_data = self.research_market_prices(product_data)
                    if not market_data:
                        failed_products.append({
                            "product": product_data,
                            "reason": "Market research failed"
                        })
                        continue
                    
                    # Step 4: Price calculation
                    calculated_prices = self.calculate_bazar_prices(product_data, market_data)
                    if not calculated_prices:
                        failed_products.append({
                            "product": product_data,
                            "reason": "Price calculation failed"
                        })
                        continue
                    
                    # Step 5: Add to database
                    new_product = self.add_to_database(product_data, market_data, calculated_prices)
                    if not new_product:
                        failed_products.append({
                            "product": product_data,
                            "reason": "Database addition failed"
                        })
                        continue
                    
                    # Track successful product
                    new_product['source_image'] = filename
                    new_product['position_in_image'] = product_position
                    successful_products.append(new_product)
                    
                    logging.info(f"  ✅ Product {i+1} -> ID {new_product['id']}: {product_data['marca']} {product_data['produto']}")
                    
                except Exception as e:
                    logging.error(f"  ❌ Failed to process product {i+1}: {e}")
                    failed_products.append({
                        "product": product_data,
                        "reason": str(e)
                    })
                    continue
            
            # Determine overall result
            total_detected = len(products_detected)
            total_successful = len(successful_products)
            total_failed = len(failed_products)
            
            if total_successful == 0:
                # No products succeeded
                raise Exception(f"Failed to process any products ({total_failed}/{total_detected} failed)")
            
            # Step 6: Move photo and log results
            shutil.move(photo_path, self.processed / filename)
            
            # Create comprehensive log entry
            log_data = {
                "filename": filename,
                "total_detected": total_detected,
                "successful": total_successful,
                "failed": total_failed,
                "successful_products": successful_products,
                "failed_products": failed_products,
                "processing_summary": f"{total_successful}/{total_detected} products added successfully"
            }
            self.log_processing(filename, "multi_success", log_data)
            
            if total_failed > 0:
                logging.warning(f"⚠️ {filename}: {total_successful}/{total_detected} products successful, {total_failed} failed")
            else:
                logging.info(f"🎉 {filename}: All {total_successful} products processed successfully!")
            
            return True
            
        except Exception as e:
            logging.error(f"❌ Failed to process {filename}: {e}")
            try:
                shutil.move(photo_path, self.failed / filename)
            except:
                pass
            self.log_processing(filename, "failed", error=e)
            return False

    def analyze_existing_photos(self):
        """Re-analyze photos in processed folder for multiple products"""
        logging.info("🔍 Starting analysis of existing processed photos...")
        
        if not self.processed.exists():
            logging.info("No processed photos found.")
            return
            
        photo_files = []
        for file_path in self.processed.iterdir():
            if (file_path.is_file() and 
                file_path.suffix.lower() in self.image_extensions):
                photo_files.append(file_path)
        
        if not photo_files:
            logging.info("No photos found in processed folder.")
            return
            
        logging.info(f"📸 Found {len(photo_files)} processed photos to re-analyze")
        
        new_products_found = 0
        
        for photo_path in photo_files:
            filename = photo_path.name
            
            try:
                logging.info(f"🔍 Re-analyzing {filename}...")
                
                # Get existing products from this image
                existing_products = self.get_products_from_image(filename)
                
                # Detect all products in image  
                all_products = self.detect_makeup_products(photo_path)
                
                if len(all_products) <= len(existing_products):
                    logging.info(f"  ➡️ No new products found ({len(all_products)} detected, {len(existing_products)} already in database)")
                    continue
                
                logging.info(f"  🎉 Found {len(all_products)} total products, {len(existing_products)} already processed")
                
                # Process only new products  
                for i, product_data in enumerate(all_products[len(existing_products):], len(existing_products) + 1):
                    if product_data.get("confidence", 0) >= 70:
                        try:
                            market_data = self.research_market_prices(product_data)
                            calculated_prices = self.calculate_bazar_prices(product_data, market_data)
                            new_product = self.add_to_database(product_data, market_data, calculated_prices)
                            
                            if new_product:
                                new_product['source_image'] = filename
                                new_product['position_in_image'] = f'additional_product_{i}'
                                new_products_found += 1
                                
                                logging.info(f"  ✅ Added product {i}: {product_data['marca']} {product_data['produto']} -> ID {new_product['id']}")
                            
                        except Exception as e:
                            logging.error(f"  ❌ Failed to process additional product {i}: {e}")
                
            except Exception as e:
                logging.error(f"❌ Failed to re-analyze {filename}: {e}")
                
        logging.info(f"🎉 Re-analysis complete! {new_products_found} new products added from existing photos.")
        
    def reprocess_folder(self, folder_name):
        """Reprocess photos from specified folder (failed or processed)"""
        if folder_name == "failed":
            source_folder = self.failed
        elif folder_name == "processed":
            source_folder = self.processed
        else:
            logging.error(f"Unknown folder: {folder_name}")
            return
            
        if not source_folder.exists():
            logging.info(f"Folder {source_folder} does not exist.")
            return
            
        photo_files = []
        for file_path in source_folder.iterdir():
            if (file_path.is_file() and 
                file_path.suffix.lower() in self.image_extensions):
                photo_files.append(file_path)
        
        if not photo_files:
            logging.info(f"No photos found in {folder_name}/ folder.")
            return
            
        logging.info(f"🔄 Reprocessing {len(photo_files)} photos from {folder_name}/ folder...")
        
        for photo_path in photo_files:
            try:
                # Copy photo to to_process for reprocessing
                temp_path = self.to_process / photo_path.name
                shutil.copy2(photo_path, temp_path)
                
                # Process the photo
                success = self.process_single_photo(temp_path)
                
                if success and folder_name == "failed":
                    # Remove from failed folder if successful
                    photo_path.unlink()
                    logging.info(f"♻️ Successfully reprocessed and removed from failed: {photo_path.name}")
                    
            except Exception as e:
                logging.error(f"❌ Failed to reprocess {photo_path.name}: {e}")
                
        logging.info(f"🎉 Reprocessing of {folder_name}/ folder complete!")
    
    def get_products_from_image(self, filename):
        """Get existing products that were processed from this image"""
        try:
            if self.data_file.exists():
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    products = json.load(f)
                
                # Find products that came from this image
                image_products = []
                for product in products:
                    if product.get('source_image') == filename:
                        image_products.append(product)
                        
                return image_products
        except Exception as e:
            logging.error(f"Failed to load existing products: {e}")
        
        return []
    
    def scan_and_process(self):
        """Scan for new photos and process them"""
        if not self.to_process.exists():
            return
            
        photo_files = []
        for file_path in self.to_process.iterdir():
            if (file_path.is_file() and 
                file_path.suffix.lower() in self.image_extensions):
                photo_files.append(file_path)
        
        if photo_files:
            logging.info(f"📸 Found {len(photo_files)} photos to process")
            
            for photo_path in photo_files:
                self.process_single_photo(photo_path)
                
        else:
            logging.debug(f"No new photos found in {self.to_process}")
    
    def run_continuous(self, interval=30):
        """Run continuous monitoring"""
        logging.info(f"🚀 Starting auto photo processor...")
        logging.info(f"📁 Monitoring: {self.to_process}")
        logging.info(f"⏱️ Check interval: {interval} seconds")
        logging.info(f"🎯 Supported formats: {', '.join(self.image_extensions)}")
        
        try:
            while True:
                self.scan_and_process()
                time.sleep(interval)
                
        except KeyboardInterrupt:
            logging.info("🛑 Auto processor stopped by user")
        except Exception as e:
            logging.error(f"💥 Auto processor crashed: {e}")

def main():
    """Main entry point with command line options"""
    import sys
    
    processor = AutoPhotoProcessor()
    
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == "--analyze-existing" or command == "-a":
            print("🔍 Analyzing existing photos for multiple products...")
            processor.analyze_existing_photos()
            return
            
        elif command == "--reprocess" or command == "-r":
            if len(sys.argv) > 2:
                folder = sys.argv[2]
                print(f"🔄 Reprocessing photos in {folder}...")
                processor.reprocess_folder(folder)
            else:
                print("❌ Please specify folder: --reprocess processed")
            return
            
        elif command == "--help" or command == "-h":
            print_help()
            return
    
    # Default: continuous monitoring
    processor.run_continuous()

def print_help():
    """Print help information"""
    print("""
🤖 Bazar da Thaís - Auto Photo Processor

USAGE:
  python auto_process.py                    # Start continuous monitoring
  python auto_process.py --analyze-existing # Re-analyze processed photos  
  python auto_process.py --reprocess failed # Reprocess failed photos
  python auto_process.py --help             # Show this help

MODES:
  🔄 Continuous    Monitor to_process/ folder automatically
  🔍 Analyze       Re-scan processed photos for missed products
  ♻️ Reprocess     Retry photos from failed/ folder
  
EXAMPLES:
  # Start auto-monitoring (normal mode)
  python auto_process.py
  
  # Re-analyze all processed photos for multiple products
  python auto_process.py --analyze-existing
  
  # Retry failed photos (after fixing issues)
  python auto_process.py --reprocess failed
  
  # Reprocess photos that were processed as single-product
  python auto_process.py --reprocess processed
    """)

if __name__ == "__main__":
    print("🤖 Bazar da Thaís - Auto Photo Processor")
    print("➡️  Drop photos in 'photos/to_process/' for automatic processing")  
    print("➡️  Multiple products per photo are now supported!")
    print("➡️  Use --help for additional commands")
    print("➡️  Press Ctrl+C to stop")
    print()
    main()